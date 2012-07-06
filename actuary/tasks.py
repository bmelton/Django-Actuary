from celery.task import Task
from celery.registry import tasks
import datetime
import requests
import datetime
import settings

class Actuary(Task):
    def run(self, user_id, page, **kwargs):
        logger = self.get_logger(**kwargs)
        logger.error("Actuary event captured.")
        ts      = datetime.datetime.now()
        print "%s - %s - %s" % (ts, user_id, page)
