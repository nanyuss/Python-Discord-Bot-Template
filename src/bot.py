import os
import logging

import discord
from discord.ext import commands

from .core.database import DatabaseManager

log = logging.getLogger(__name__)

#Classe principal da aplicação.
class MyBot(commands.Bot):
	def __init__(self):
		super().__init__(
			intents=discord.Intents.all(), #Definindo que todas as intents da aplicação serão ativadas.
			command_prefix='..', #Prefixo da aplicação.
		)
		self.db: DatabaseManager = None
		
	#Função que carrega todas as extensões (cogs).
	async def load_cogs(self, path: str):
		for root, _, files in os.walk(path.replace('/', os.path.sep)):
			for file in files:
				if file.endswith('.py'):
					try:
						await self.load_extension(os.path.join(root, file)[:-3].replace(os.path.sep, '.'))
						log.debug(f'✅Carregado {file!r} de {root[9:]!r}.')
					except Exception:
						log.exception(f'❌Falha ao carregar {file!r} de {root[9:]!r}:')

	#Evento chamado enquanto a aplicação inicia.
	async def setup_hook(self):
		pass
	
	#Evento chamado quando a aplicação está pronta para ser utilizada.
	async def on_ready(self):
		log.info(f'Conectado como {self.user} ({self.user.id}).')
		log.info(f'Latência: {round(self.latency * 1000)}ms.')

	#Evento chamado quando a aplicação está se conectando.
	async def start(self, token, *, reconnect = True):
		self.db = await DatabaseManager().connect()
		await self.load_cogs('src/cogs')
		return await super().start(token, reconnect=reconnect)
	
	#Evento chamado quando a aplicação está se desconectando.
	async def close(self):
		log.info('Desconectando...')
		await super().close()