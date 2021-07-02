from db import BaseCRUD
from tusers import models, schemas


crud = BaseCRUD[
    models.TwitterUser, models.TwitterUserMetrics, schemas.TUserCreate, schemas.TUserUpdate
](models.TwitterUser, models.TwitterUserMetrics)
