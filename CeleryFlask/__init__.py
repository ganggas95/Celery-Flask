import flask
from celery import Celery


class CeleryFlask(Celery):

    def __init__(self, app=None, *args, **kwargs):
        super(CeleryFlask, self).__init__(*args, **kwargs)
        self.patch_task()
        if app:
            self.init_app(app)

    def patch_task(self):
        BaseTask = self.Task
        _celery = self

        class ContextTask(BaseTask):
            abstract = True

            def __call__(self, *args, **kwargs):
                if flask.has_app_context():
                    return BaseTask.__call__(self, *args, **kwargs)
                with _celery.app.app_context():
                    return BaseTask.__call__(self, *args, **kwargs)

        self.Task = ContextTask

    def init_app(self, app):
        self.app = app
        self.config_from_object(app.config)
