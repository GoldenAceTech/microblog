from dotenv import dotenv_values

config = dotenv_values(".env")


class Config:
    """Base config for flask app."""

    SECRET_KEY = config.get("SECRET_KEY")
    DATABASE = config.get("DATABASE")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    TESTING = False
    DEBUG = False


class ProdConfig(Config):
    """App config for production"""

    ENV = "production"
    MONGO_URI = config.get("PROD_MONGO_URI")


class DevConfig(Config):
    """App config for development"""

    ENV = "development"
    DEBUG = True
    TESTING = True
    MONGO_URI = config.get("DEV_MONGO_URI")

class TestConfig(DevConfig):
    """App config for testing

    Args:
        Config (DevConfig): The development config class
    """

    ENV = "testing"
    DATABASE = config.get("TEST_DATABASE")
    MONGO_URI = config.get("TEST_MONGO_URI")
    SECRET_KEY = config.get("TEST_SECRET_KEY")