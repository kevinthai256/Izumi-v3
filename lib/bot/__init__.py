import discord
from discord.utils import find
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound, BadArgument, MissingRequiredArgument, MissingRole, MissingPermissions, CommandOnCooldown
import os
from discord.errors import Forbidden
from discord import Embed, File, Intents
from glob import glob
from datetime import datetime, timezone
from asyncio import sleep
from lib.util.info import InfoTemplate
from lib.util.colors import colord
from lib.util.statuses import status
from lib.util.funtions import boldText
from lib.util.funtions import update_user
from lib.util.funtions import update_xp
import random
import asyncio
from asyncio import sleep
from replit import db
from lib.commands.general import setup as General


intents = discord.Intents.all()
intents.message_content = True
activity= discord.Game(name=".cmd")
bot = commands.Bot(command_prefix = '.', intents=intents,  help_command=None, activity=activity)

prefix = '.'


botname = str(bot.user)
botnick = str(bot.user)
token = os.environ['token']

INTENTS = discord.Intents.all()

PREFIX = "."
OWNER_IDS = [424652015227109376]
COMMANDS = [path.split("/")[-1][:-3] for path in glob("./lib/commands/*.py")]
IGNORE_EXCEPTIONS = [CommandNotFound, CommandOnCooldown,BadArgument, IndexError]
class Ready(object):
    def __init__(self):
        for command in COMMANDS:
            setattr(self, command, False)
        
    def ready_up(self, command):
        setattr(self, command, True)
        print(f"{command} commands are ready.")

    def all_ready(self):
        return all([getattr(self, command) for command in COMMANDS])

class Bot(commands.Bot):
    prefix = '.'
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.command_ready = Ready()
        self.guild = None
        

        super().__init__(command_prefix=PREFIX, OWNER_ID=OWNER_IDS, intents=intents, help_command=None)
      
    
      
    async def setup(self):
        print("setup Run")
        
        for command in COMMANDS:
            await self.load_extension(f"lib.commands.{command}")
            print(f"{command} cog Loaded")

    def run(self, token):
        print("running setup")
        self.setup()
        self.TOKEN = token
        print("Running Bot...")
        super().run(self.TOKEN, reconnect=True)
        

    async def process_commands(self,origin):
        ctx = await self.get_context(origin, cls=Context)
      
        if ctx.command is not None:
          await self.invoke(ctx) 
        else:
          print(ctx.command)
    
    async def on_connect(self):
        print("Konichiwa Senpai!")
        
    async def on_disconnect(self):
        print("Ara ara, sayanora!")
        await self.change_presence(status=discord.Status.idle,          activity=discord.Game("Bot Offline."))


    async def on_error(self, err, ctx, *args, **kwargs):
        if err == 'on_command_error':
            await ctx.send("An error Occurrred")
        raise 

    async def on_command_error(self, ctx, exc):
      if isinstance(exc, commands.CommandOnCooldown):
        secs = '{:.2f}'.format(exc.retry_after)
        mins = round(int(float(secs)) // 60)
        if round(float(secs)) < 60:
          msg = f'**Almost!** You can try again in {secs} seconds.'
        else:
          msg = f'**Still on cooldown!** Thanks for your care for the enviroment, but you can plant a tree again in {mins} minutes! :D'
        embed = discord.Embed(title=msg, color=colord['Green'])
        await ctx.send(embed=embed)
        
        if any([isinstance(exc, err) for err in IGNORE_EXCEPTIONS]):
            pass

        elif isinstance(exc, MissingRequiredArgument):
            await ctx.send("One or More argument required!")

        elif isinstance(exc, MissingPermissions):
            await ctx.send("You are not allowed to do that.")

        elif isinstance(exc, MissingRole):
            await ctx.send("You do not have the necessary role to do that.")
        
        elif hasattr(exc, "original"):
            if isinstance(exc.original, Forbidden):
                await ctx.send("I don't have permission to do that!!")
            else:
                raise exc.original
        else:
            raise exc



  
    async def on_guild_join(self, guild):
      x = datetime.now()

      pdthr = int(x.strftime("%I")) + 5

      if pdthr > 12:
        hr = str(pdthr - 12)
        ampm = 'pm'
      else:
        hr = str(pdthr)
        ampm = 'am'

      minute = int(x.strftime("%M"))

      message = f'Today at: {hr}:{minute}{ampm}'
      general = str.find(lambda x: x.name == 'general', guild.text_channels)
  
      if general and general.permissions_for(guild.me).send_messages:
        embed = discord.Embed(title=f"{bot.name} is now in your server!", description="Hello! Thanks for inviting me, you're such a nice server!", colour=0x00FFFF)
        embed.set_author(name=guild.name)
        embed.set_thumbnail(url=bot.avatar.url)
        embed.set_footer(message)
        await general.send(embed=embed)
    
    async def on_message(self, message):
        await self.process_commands(message)


      

bot = Bot()