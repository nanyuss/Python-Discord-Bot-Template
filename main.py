import asyncio
import logging
import os

from dotenv import load_dotenv
from src.bot import MyBot

logging.basicConfig(level=logging.INFO, format='%(name)s | %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

load_dotenv()
log.info('Iniciando aplicação...')

async def main():
    async with MyBot() as bot:
        await bot.start(os.getenv('TOKEN'))

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
except Exception:
    log.exception('Ocorreu um erro ao iniciar a aplicação:')