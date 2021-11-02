from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASDE_URI")
    app.config['SQLALCHEMY_ECHO'] = True 

    # Import models here
    from app.models.book import Book

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app
