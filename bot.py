import discord
from discord.ext import commands
from bot_logic import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="$", intents=intents)
#ESto es un cambio
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()    
async def password(ctx):
    await ctx.send(gen_pass(10))      

bot.run("")
