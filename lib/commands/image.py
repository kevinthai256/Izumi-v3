
from discord.ext.commands import Cog, command, has_permissions, has_role
import discord
from discord import Member
from discord import Embed,File
from typing import Optional
from random import choice
from asyncio import TimeoutError, sleep
from lib.util.convert_time import convert
from discord.ext import commands
from lib.util.colors import colord
from lib.util.functions import action, RandomGif, boldText



#image commands

class Image(Cog):
    def __init__(self,bot):
        self.bot = bot

#GIF
    @command(aliases=['gif'])
    async def g(self, ctx, *, search=None):
      if not search:
        search = "gif"

      gifsearch = (action((search)))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(color=colord['Yellow'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)
      print(gif)

#displays image
    @command(aliases=['image'])
    async def img(self, ctx, *, link):
  
      embed = discord.Embed(color=colord['White'])
      embed.set_image(url=link)

      await ctx.channel.purge(limit=1)
      await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("image")
            
async def setup(bot):
    await bot.add_cog(Image(bot))
