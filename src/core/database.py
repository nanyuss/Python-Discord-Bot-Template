import os
import logging
import aiosqlite
from motor.motor_asyncio import AsyncIOMotorClient
from .config_load import Config

log = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self):
        self._mongo_uri = Config.MONGO
        self._sqlite_path = 'database.db'
        self.database = None
        self.db_type = 'MongoDB' if self._is_valid_uri() else 'SQLite'

    # Verifica se a URI do MongoDB é válida.
    def _is_valid_uri(self):
        try:
            client = AsyncIOMotorClient(self._mongo_uri, serverSelectionTimeoutMS=1000)
            client.server_info()
            return True
        except Exception as e:
            return False
        
    # Conecta ao banco de dados.
    async def connect(self):
        if self.db_type == 'MongoDB':
            self.client = AsyncIOMotorClient(self._mongo_uri)
            self.database = self.client['global']
        else:
            if not os.path.exists(self._sqlite_path):
                with open('init.sql') as file:
                    script = file.read()
                async with aiosqlite.connect(self._sqlite_path) as conn:
                    await conn.executescript(script)
            
            self.database = await aiosqlite.connect(self._sqlite_path)
            
        log.info(f'Conectado ao banco de dados {self.db_type}.')
        
        return self
