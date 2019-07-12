from flask import Flask, url_for
from flask_navigation import Navigation
from flask_sqlalchemy import SQLAlchemy

from .config import Config
config = Config()

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


from .routes import main_bp

with app.app_context():
    app.register_blueprint(main_bp)

# navigation: https://flask-navigation.readthedocs.io
nav = Navigation(app)
nav.Bar('top', [
    nav.Item('Home', 'main_bp.home'),
    nav.Item('About', 'main_bp.about'),
])
