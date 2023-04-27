import os
from os.path import join, dirname

from pathlib import Path
from dotenv import load_dotenv,find_dotenv

# dotenv_path = join(dirname(__file__),'.env')
# load_dotenv(dotenv_path)
load_dotenv(find_dotenv())

class Settings: 
    PROJECT_TITLE: str =os.environ.get("PROJECT_TITLE")
    PROJECT_VERSION: str = os.environ.get("PROJECT_VERSION")   

    SECRET_KEY: str =os.environ.get("SECRET_KEY")

    
    POSTGRES_USER :str =os.environ.get("POSTGRES_USER")
    # POSTGRES_USER :str =os.getenv("POSTGRES_USER","postgres")
    POSTGRES_PASSWORD =os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER :str =os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT :str =os.getenv("POSTGRES_PORT")
    POSTGRES_DB :str =os.getenv("POSTGRES_DB")
    POSTGRES_URL  = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

#   SMTP
    SMTP_user: str = os.getenv("SMTP_USER")
    SMTP_pwd: str = os.getenv("SMTP_PWD")

settings = Settings()