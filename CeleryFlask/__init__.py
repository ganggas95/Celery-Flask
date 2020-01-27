# -*- coding: utf-8 -*-
"""
    Celery Flask
    ~~~~~~~~
    Celery integrated to Flask App
    :copyright: (c) 2019-2020 Subhan Nizar <subhannizar25@gmail.com>
    :license: MIT License (MIT), see LICENSE for more details.
"""
import flask
from celery import Celery


class CeleryFlask(Celery):
    """Celery Flass class"""

    def __init__(self, app=None, *args, **kwargs):
        super(CeleryFlask, self).__init__(*args, **kwargs)
        self.patch_task()
        if app:
            self.init_app(app)

    def patch_task(self):
        """Method to handle patching  new task"""
        BaseTask = self.Task
        _celery = self

        class ContextTask(BaseTask):
            """Class context task"""
            abstract = True

            def __call__(self, *args, **kwargs):
                if flask.has_app_context():
                    return BaseTask.__call__(self, *args, **kwargs)
                with _celery.app.app_context():
                    return BaseTask.__call__(self, *args, **kwargs)

        self.Task = ContextTask

    def init_app(self, app):
        """Initialize your flask app to this library using this method"""
        self.app = app
        if app:
            self.conf.update(app.config)
