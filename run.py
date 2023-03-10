from flask import Flask
from flask_restx import Api
from flask_restx.representations import output_json

from app.setup_bd import db
from app.api.api_views import api_blueprint

from app.views.movies import movies_ns
from app.views.directors import directors_ns
from app.views.genres import genres_ns

from app.config import Config


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()  # Требуется для применения конфига ко всему приложению
    configure_app(application)

    return application


def configure_app(application: Flask) -> None:
    db.init_app(application)
    api = Api(application)
    api.representations = {'application/json; charset=utf-8': output_json}

    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


app_config = Config()
app = create_app(app_config)

app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
