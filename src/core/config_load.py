import os
from dotenv import load_dotenv
from dataclasses import dataclass

class Config:
    PREFIX = os.getenv('PREFIX' , '..')
    MONGO = os.getenv('MONGO' , '')

    def getenv(key, default=None):
        return os.getenv(key, default)