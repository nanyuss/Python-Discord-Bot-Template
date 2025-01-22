import os
from dotenv import load_dotenv
from dataclasses import dataclass

null_and_bool = {
    'true': True,
    'false': False,
    'None': None
}

DEFAULT_CONFIG = {
    'PREFIX': '..',  # Prefixo padrão
    'MONGO': '',     # URL do MongoDB, vazio se não estiver definido
}

class Config:
    PREFIX = os.getenv('PREFIX' , '..')
    MONGO = os.getenv('MONGO' , '')

    def getenv(key, default=None):
        return os.getenv(key, default)