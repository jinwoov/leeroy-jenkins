from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    register_blueprints(app)
    return app


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from src.api import bp_flask

    app.register_blueprint(bp_flask)
