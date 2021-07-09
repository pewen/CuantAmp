from typing import (
    Any,
    Dict,
    Generic,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declarative_base
from fastapi.encoders import jsonable_encoder


SQLBaseModel = declarative_base()


class BaseModel(SQLBaseModel):
    "Base model for all DB entities"
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    _created_at = Column(
        DateTime(timezone=True),
        default=func.now(),
    )
    _updated_at = Column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
    )


# Base schema with map from camelCase to snake_case
def to_camel(string: str) -> str:
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


class BaseSchema(PydanticBaseModel):
    id: int

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


ModelType = TypeVar("ModelType", bound=BaseModel)
MetricsModelType = TypeVar("MetricsModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=PydanticBaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PydanticBaseModel)


def fill_model(data: dict, model: BaseModel):
    columns = [c.name for c in inspect(model).columns]
    data = {key: value for key, value in data.items() if key in columns}
    return model(**data)

class BaseCRUD(Generic[ModelType, MetricsModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self, model: Type[ModelType], metrics_model: Type[MetricsModelType]
    ):
        """
        CRUD object with default methods to
        Create, Read, Update, Delete (CRUD)
        object with its associated metrics.
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `metrics_model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.metrics_model = metrics_model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).one_or_none()

    def get_multi(self, db: Session, *, order=["id"]) -> List[ModelType]:
        return (
            db.query(self.model)
            .order_by(*get_ordering_for_model(self.model, order))
            .all()
        )

    def get_metrics(self, db: Session, *, by: dict, order=["time desc"]) -> List[MetricsModelType]:
        return (
            db.query(self.metrics_model)
            .filter_by(**by)
            .order_by(*get_ordering_for_model(self.metrics_model, order))
            .all()
        )

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        if isinstance(obj_in, dict):
            create_data = obj_in
        else:
            create_data = obj_in.dict(exclude_unset=True)
        db_obj = fill_model(create_data, self.model)
        db.add(db_obj)
        db_metrics_obj = fill_model(create_data, self.metrics_model)
        db.add(db_metrics_obj)

        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)

        if "id" in update_data:
            del update_data["id"]
        db_metrics_obj = fill_model(update_data, self.metrics_model)
        db.add(db_metrics_obj)

        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj


def get_ordering_for_model(model, order=["id"]):
    return [
        getattr(model, field.replace(" desc", "")).desc()
        if field.endswith(" desc")
        else getattr(model, field)
        for field in order
    ]
