# Actuary, a Django Auditing app
# by Barry Melton, 7/5/2012
# MIT-licensed - http://www.opensource.org/licenses/mit-license.php/

import datetime
import settings

import logging
logger = logging.getLogger('django')

# Should import settings.  There are settings values that need to be set, 
# namely, 
# ACTUARY_USE_CELERY, default = False
# ACTUARY_APIKEY, default = None, but will err if not present
# ACTUARY_TRACK_AJAX, default = False. 
try: 
    settings.ACTUARY_USE_CELERY
except NameError:
    settings.ACTUARY_USE_CELERY=True

try:
    settings.ACTUARY_USE_MONGO
except NameError:
    settings.ACTUARY_USE_MONGO=False

try: 
    settings.ACTUARY_TRACK_AJAX
except NameError:
    settings.ACTUARY_TRACK_AJAX=True

class ActuaryMiddleware(object):
    def process_request(self, request):
        log_dict = {} 
        if request.is_ajax():
            if settings.ACTUARY_TRACK_AJAX: 
                if not request.user is None:
                    log_dict["user"] = request.user.id
                else:
                    log_dict["user"] = 0
                log_dict["timestamp"] = datetime.datetime.now()
                log_dict["host"] = request.get_host()
                log_dict["method"] = request.method
                log_dict["path"] = request.path    
                log_dict["full_path"] = request.get_full_path()
                log_dict["raw_post"] = request.raw_post_data
            else:
                # We aren't logging AJAX requests, so we'll just pass here.
                pass

        print log_dict

        if settings.ACTUARY_USE_CELERY:
            from actuary.tasks import Actuary
            pass
