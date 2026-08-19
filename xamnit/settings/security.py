import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "false").lower()

DEV_ALLOWED_HOSTS = "localhost" if DEBUG == "true" else ""

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", DEV_ALLOWED_HOSTS).split(",")
