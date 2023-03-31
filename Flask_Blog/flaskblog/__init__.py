from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flaskblog.config import Config
from flask_dance.contrib.google import make_google_blueprint

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info' # info is bootstrap class blue colored allert
mail = Mail()


def create_app(config_class=Config):
    app = Flask("flaskblog")
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Google Blueprint'ını oluştur
    google_bp = make_google_blueprint(
        client_id="655299075419-u3kjofupjh2n8oe3cqh341k89g86q9j6.apps.googleusercontent.com",
        client_secret="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",
        scope=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"],
        redirect_to="http://localhost:5000/auth/google/callback"
    )

    # Uygulamaya Blueprint'ı ekle
    app.register_blueprint(google_bp, url_prefix="/login")

    from flaskblog.errors.handlers import errors
    from flaskblog.main.routes import main
    from flaskblog.posts.routes import posts
    from flaskblog.users.routes import users
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    with app.app_context():
        db.create_all()

    return app