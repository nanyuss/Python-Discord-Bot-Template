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

class ConfigLoader:
    def __init__(self):
        load_dotenv()
        self.config = DEFAULT_CONFIG

    def load(self):
        for key, value in DEFAULT_CONFIG.items():
            env_value = os.getenv(key)
            if env_value:
                self.config[key] = null_and_bool.get(env_value, env_value)
        return self.config
    
class Config:
    to_dict = ConfigLoader().load()

    PREFIX = to_dict['PREFIX']
    MONGO = to_dict['MONGO']