from pymongo import MongoClient
import datetime
import time

class Logs(object):

    def __init__(self):

        self.client = MongoClient()
        self.db = self.client.mongo
        self.errors = self.db.errors
	self.ts = time.time()
        self.st = datetime.datetime.fromtimestamp(self.ts).strftime('%Y-%m-%d %H:%M:%S')


    def insert_error(self, logs):

        err_logs = {
	    "date": self.st,
            "error": logs
        }

        error_logs = self.errors.insert(err_logs)

