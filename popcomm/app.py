from flask import Flask
from celery import Celery
from werkzeug.debug import DebuggedApplication


from popcomm.blueprints.contact import contact
from popcomm.extensions import debug_toolbar, mail, csrf

CELERY_TASK_LIST = [
    'popcomm.blueprints.contact.tasks',
]


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(contact)
    extensions(app)

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    return None
