import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev_key"
    
    MYSQL_USER = os.environ.get("DB_USER") or "root"
    MYSQL_PASSWORD = os.environ.get("DB_PASSWORD") or "password"
    MYSQL_DB = os.environ.get("DB_NAME") or "reverse_classroom"
    MYSQL_HOST = os.environ.get("DB_HOST") or "localhost"
    MYSQL_PORT = int(os.environ.get("DB_PORT") or 3306)

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
