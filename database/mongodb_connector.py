import os

import pymongo
from cron_utils.load_env import *


class DatabaseSession:
    def __init__(self):
        self.mongodb_dict = {
            "MONGODB_URL": os.getenv("MONGODB_URL_LOCAL") if os.getenv("ENV") == "local" else os.getenv(
                "MONGODB_URL_PROD"),
            "ADMIN_DATABASE_NAME": os.getenv("ADMIN_DATABASE_NAME"),
            "USER_COLLECTION_NAME": os.getenv("USER_COLLECTION_NAME"),
            "AnalyticsLayerDetails": {
                "USER_SESSION": os.getenv("USER_SESSION"),
                "SESSION_LAYER": os.getenv("SESSION_LAYER")
            },
        }

        self.client = pymongo.MongoClient(self.mongodb_dict["MONGODB_URL"])
        self.admin_database = self.client[self.mongodb_dict["ADMIN_DATABASE_NAME"]]
        self.user_collection = self.admin_database[self.mongodb_dict["USER_COLLECTION_NAME"]]
        self.user_session_layer = self.mongodb_dict["AnalyticsLayerDetails"]["USER_SESSION"]
        self.session_layer = self.mongodb_dict["AnalyticsLayerDetails"]["SESSION_LAYER"]


session = DatabaseSession()
