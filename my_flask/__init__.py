from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__, static_folder='static')
app.config.from_object(config['flask_db'])
db = SQLAlchemy(app)

def create_app():
    db.init_app(app)

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    return app
