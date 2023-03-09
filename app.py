from flask import Flask

from core.models.model import db
from core.api.api_views import api_blueprint

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)

app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
