ACTUARY
==========

Actuary aims to be a complete auditing solution for Django, with optional 
support for Mongo as a backend store (using mongoengine) or Django's ORM, as 
well as support for using Celery with bundled Tasks. 

Actuary uses middleware to capture page views, signals for capturing model 
changes, and a callable for tracking custom events. 

This is super pre-alpha at this stage, and you should not download it as it
will almost certainly destroy your server. 

Installation
============

Clone it to actuary and include actuary in your settings.py

If you want super-paranoid logging, also add 
    'actuary.middleware.ActuaryMiddleware',
to your 'MIDDLEWARE CLASSES'. 

There are a few settings you need to be aware of, namely: 
* ACTUARY_USE_CELERY = True
    - This will use Celery.  The goal is to work with or without celery, and 
    there are compelling reasons not to, but I'm not developing this in a 
    sensitive environment, so I am using Celery for performance.  Make sure 
    your selection matches your environment and application requirements.

* ACTUARY_USE_MONGO  = True
    - I am developing with Mongo, and it IS the preferred method (if you ever 
    want to see your data again anyway), but we aim to have support for 
    regular ORM as well.

* ACTUARY_TRACK_AJAX = True
    - This only exists as an option to keep from periodic-polling requests to keep from 
    filling your audit log.  It should almost certainly be on by default.

LICENSE
=======

Actuary is MIT-licensed.
www.opensource.org/licenses/mit-license.php/

