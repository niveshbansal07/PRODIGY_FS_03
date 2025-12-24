import os

dbconfig = {
    "host" : "localhost",
    "user" : "root",
    "password" : "PASSWORD",
    "database" : "DATABASE_NAME"
}

SECRET_KEY = os.environ.get("YOUR_SUPER_KEY", "dev-flask-secret-key")
JWT_SECRET = os.environ.get("YOUR_SECRET_KEY", "dev-jwt-secret-key")
JWT_EXP_HOURS = 8