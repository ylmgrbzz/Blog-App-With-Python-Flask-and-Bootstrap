import os


class Config:
    SECRET_KEY ='5c2d06c9304afa76925b4b82ab092102'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    GOOGLE_CLIENT_ID = 'your_client_id'
    GOOGLE_CLIENT_SECRET = 'your_secret_key'
    GOOGLE_OAUTH_REDIRECT_URL = "callback_redirect_url"
    # for_example = http://localhost:5000/auth/google/callback
