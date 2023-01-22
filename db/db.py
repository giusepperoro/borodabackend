import databases
import sqlalchemy

import ormar

database = databases.Database("sqlite:///db.sqlite")
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
