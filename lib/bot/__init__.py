from discord.utils import find
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound, BadArgument
from discord.ext.commands import MissingRequiredArgument, MissingRole, MissingPermissions
from discord.errors import Forbidden
from discord import Embed, File, Intents
import os
from glob import glob
from datetime import datetime, timezone
from asyncio import sleep
import discord
from prsaw import RandomStuff
from lib.util.info import InfoTemplate
from lib.util.colors import colord
from lib.util.statuses import status
from lib.util.functions import boldText
import random
from discord.ext import tasks

intents = discord.Intents.all()
prefix = '.'

PREFIX = "."
OWNER_IDS = [424652015227109376]
COMMANDS = [
    os.path.basename(path)[:-3] 
    for path in glob("./lib/commands/*.py") 
    if not path.endswith("__init__.py")
]
IGNORE_EXCEPTIONS = [CommandNotFound, BadArgument]

class Ready(object):
    def __init__(self):
        for command in COMMANDS:
            setattr(self, command, False)

    def ready_up(self, command):
        setattr(self, command, True)
        print(f"{command} commands are ready.")

    def all_ready(self):
        return all([getattr(self, command) for command in COMMANDS])

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.command_ready = Ready()
        self.guild = None
        super().__init__(command_prefix=PREFIX, intents=intents, owner_ids=OWNER_IDS)

    async def setup_hook(self):
        print("setup Run")
        for command in COMMANDS:
            await self.load_extension(f"lib.commands.{command}")
            print(f"{command} cog Loaded")

    @tasks.loop(seconds=10)
    async def status_loop(self):
        """Rotate bot status"""
        await self.change_presence(
            status=discord.Status.idle,
            activity=discord.Game(random.choice(status))
        )

    @status_loop.before_loop
    async def before_status_loop(self):
        """Wait until bot is ready before starting status loop"""
        await self.wait_until_ready()

    def run(self, token, **kwargs):
        self.TOKEN = token
        print("Running Bot...")
        super().run(self.TOKEN, reconnect=True, **kwargs)

    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=Context)
        if ctx.command is not None and ctx.guild is not None:
            await self.invoke(ctx)

    async def on_connect(self):
        print("Welcome back!")

    async def on_disconnect(self):
        print("Bye bye!")

    async def on_error(self, event, *args, **kwargs):
        raise 

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, commands.CommandOnCooldown):
            secs = '{:.2f}'.format(exc.retry_after)
            mins = round(int(float(secs)) // 60)
            if round(float(secs)) < 60:
                msg = f'**Still on cooldown**, please try again in {secs} seconds.'
            else:
                msg = f'**Still on cooldown**, please try again in {mins} minutes.'
            await ctx.send(msg)
            return

        if any([isinstance(exc, err) for err in IGNORE_EXCEPTIONS]):
            pass
        elif isinstance(exc, MissingRequiredArgument):
            await ctx.send("One or More argument required!")
        elif isinstance(exc, MissingPermissions):
            await ctx.send("You are not allowed to create Giveaways.")
        elif isinstance(exc, MissingRole):
            await ctx.send("You do not have the necessary role to create Giveaways.")
        elif hasattr(exc, "original"):
            if isinstance(exc.original, Forbidden):
                await ctx.send("I don't have permission to do that!!")
            else:
                raise exc.original
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            while not self.command_ready.all_ready():
                print("waiting......")
                await sleep(0.5)
            self.ready = True
            print("Bot ready")
            # Start status loop after bot is fully ready
            if not self.status_loop.is_running():
                self.status_loop.start()

    async def on_message(self, message):
        # Don't process bot messages
        if message.author.bot:
            return

        await self.process_commands(message)

bot = Bot()