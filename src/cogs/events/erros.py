import difflib
import discord
from discord.ext import commands

from ...core.utils import permissions

from ...bot import MyBot

class CommandsErros(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot: MyBot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        _P = permissions()
        embed = discord.Embed(color=discord.Color.red())

        # Tratamento para erro de comando não encontrado
        if isinstance(error, commands.errors.CommandNotFound):
            cmd = ctx.invoked_with
            cmds = [cmd.name for cmd in self.bot.commands if not cmd.hidden]  # Listar comandos principais
            cmds = difflib.get_close_matches(cmd, cmds)  # Verificar comandos mais próximos

            # Exibir a sugestão do comando
            if cmds:
                embed.title = 'Comando não encontrado ❌'
                embed.description = f'Você quis dizer "{cmds[0]}"?'
            else:
                embed.title = 'Comando não encontrado ❌'
                embed.description = f'Comando "{cmd}" não encontrado.'

        # Tratamento para erro de argumento obrigatório
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            embed.title = 'Argumento Faltando ❌'
            embed.description = f'Argumento **{error.param.name}** é obrigatório.'

        # Tratamento para erro de permissões faltando do usuário
        elif isinstance(error, commands.errors.MissingPermissions):
            perms = [ _P.get(name) for name in error.missing_permissions if _P.get(name) ]
            perms_message = '\n'.join(sorted(perms))
            
            embed.title = 'Permissões Faltando ❌'
            if len(perms) == 1:
                embed.description = f'Você precisa da seguinte permissão para executar este comando:\n**{perms_message}**'
            else:
                embed.description = f'Você precisa das seguintes permissões para executar este comando:\n**{perms_message}**'

        # Tratamento para erro de permissões faltando do bot
        elif isinstance(error, commands.errors.BotMissingPermissions):
            perms = [ _P.get(name) for name in error.missing_permissions if _P.get(name) ]
            perms_message = '\n'.join(sorted(perms))
            
            embed.title = 'Permissões Faltando ❌'
            if len(perms) == 1:
                embed.description = f'Eu preciso da seguinte permissão para executar este comando:\n**{perms_message}**'
            else:
                embed.description = f'Eu preciso das seguintes permissões para executar este comando:\n**{perms_message}**'

        # Enviar a mensagem final com o erro
        await ctx.send(embed=embed, delete_after=5)

# Função para adicionar o Cog
async def setup(bot: MyBot):
    await bot.add_cog(CommandsErros(bot))
