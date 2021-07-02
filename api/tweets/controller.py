from db import BaseCRUD
from tweets import models, schemas


crud = BaseCRUD[
    models.Tweet, models.TweetMetrics, schemas.TweetCreate, schemas.TweetUpdate
](models.Tweet, models.TweetMetrics)
