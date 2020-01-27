# Celery integrated with Flask

## Project description

This library created for help our project using flask and celery as tasking management


### Installation

To using this library, you need to install from ```pip``` using this command
```pip install celeryflask```


### Examples

To use this library you just add following code to your project:

```
from flask import Flask
from CeleryFlask import CeleryFlask

app = Flask(__name__)
celery_flask = CeleryFlask(app)
# or
celery_flask = CeleryFlask()
celery_flask.init_app(app)

@celery_flask.task
def hello():
    print("Hello")
```

Before running celery, don't forget to add this configuration to you application config/settings:
```
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", None)
    CLEERY_BACKEND = CELERY_BROKER_URL
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", None)
    CELERY_DEFAULT_QUEUE = 'default'

    CELERY_IMPORTS = (
        # Add task here to use relative import task
    )
    # CELERY_TASK_RESULT_EXPIRES = 30
    CELERY_TIMEZONE = 'UTC'
    USE_TZ = True
    CELERY_ENABLE_UTC = False
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_RESULT_EXPIRES = 120  # 2 mins
    CELERYD_CONCURRENCY = 6
    CELERYD_MAX_TASKS_PER_CHILD = 4
    CELERYD_PREFETCH_MULTIPLIER = 1
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
    CELERY_DEFAULT_QUEUE = 'your task queue'

    CELERY_QUEUES = (
        Queue('default', Exchange('default'), routing_key='default'),
        Queue('your task queue', Exchange('your task queue'), routing_key='your task routing '),
    )
```