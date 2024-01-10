from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions, has_role
import discord
from discord import Member
from discord import Embed, File
from typing import Optional
from random import choice
from asyncio import TimeoutError, sleep
from lib.util.convert_time import convert
from discord.ext import commands
import discord
from discord import Member
from replit import db
import nekos
import random
from discord import Embed, File
from lib.util.colors import colord

from lib.util.funtions import action
from lib.util.funtions import RandomGif
from lib.util.funtions import addlog

from lib.util.actions import adjectives, eactions, actions, Sactionsdef, actionsdef


class Action(Cog):

  def __init__(self, bot):
    self.bot = bot
    self.cancelled = False


#baka

  @command(name="baka", aliases=[])
  async def baka(self, ctx, *, member: discord.Member = None):
    if member == None:
      response = 'BAKA!'
    else:
      response = f"You are a baka, {member.name}!"

    gifsearch = (action(("baka")))
    giflink = RandomGif(gifsearch)
    gif = giflink.replace("'", ' ').replace(",", ' ')

    embed = discord.Embed(title=response, color=colord['Teal'])
    embed.set_image(url=gif)

    await ctx.send(embed=embed)

  #action
  @commands.cooldown(1, 5, commands.BucketType.member)
  @command(name='call', aliases=actions)
  async def call_action(self, ctx, *, member: discord.Member = None):
    if member == None:
      if ctx.invoked_with in actionsdef:
        response = ctx.author.name + " is " + actionsdef[
          ctx.invoked_with] + "!"
      else:
        response = ctx.author.name + " is " + ctx.invoked_with + "ing" + "!"
    else:
      if str(ctx.invoked_with) in Sactionsdef:
        response = f"{ctx.author.name} is {Sactionsdef[str(ctx.invoked_with)]} {member.name}!"
      else:
        response = ctx.author.name + " is " + ctx.invoked_with + "ing  " + member.name + "!"
    if ctx.invoked_with == "hell":
      response = ctx.author.name + " is sending " + member.name + " to hell!"
    if ctx.invoked_with == "superhell":
      response = ctx.author.name + " is sending " + member.name + " to super hell!"

    gifsearch = (action(("anime" + ctx.invoked_with)))
    if ctx.invoked_with == "sex":
      gifsearch = (action(("beidou")))
    giflink = RandomGif(gifsearch)
    gif = giflink.replace("'", ' ').replace(",", ' ')

    embed = discord.Embed(title=response, color=colord['Teal'])
    embed.set_image(url=gif)
    await ctx.message.delete()
    await ctx.send(embed=embed)
    print(gif)
    if "Izumi" in response:
      if str(ctx.invoked_with) in Sactionsdef:
        response = f"I'm {Sactionsdef[str(ctx.invoked_with)]} {ctx.author.name} back!"
      else:
        response = "I'm " + ctx.invoked_with + "ing  " + ctx.author.name + " back!"

      gifsearch = (action(("anime" + ctx.invoked_with)))
      if ctx.invoked_with == "sex":
        gifsearch = (action(("beidou")))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Teal'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)

  #action
  @commands.cooldown(1, 5, commands.BucketType.member)
  @command(aliases=eactions)
  async def wave(self, ctx, *, member: discord.Member = None):
    await ctx.message.delete()
    if member == None:
      if ctx.invoked_with in actionsdef:
        response = ctx.author.name + " is " + actionsdef[
          ctx.invoked_with] + "!"
      else:
        response = ctx.author.name + " is " + ctx.invoked_with[:-1] + "ing" + "!"
    else:
      if str(ctx.invoked_with) in Sactionsdef:
        response = f"{ctx.author.name} is {Sactionsdef[str(ctx.invoked_with)]} {member.name}!"
      else:
        response = ctx.author.name + " is " + ctx.invoked_with[:
                                                               -1] + "ing  " + member.name + "!"

    gifsearch = (action(("anime" + ctx.invoked_with)))
    giflink = RandomGif(gifsearch)
    gif = giflink.replace("'", ' ').replace(",", ' ')

    embed = discord.Embed(title=response, color=colord['Teal'])
    embed.set_image(url=gif)
    await ctx.send(embed=embed)
    print(gif)
    if "Izumi" in response:
      if str(ctx.invoked_with) in Sactionsdef:
        response = f"I'm {Sactionsdef[str(ctx.invoked_with)]} {ctx.author.name} back!"
      else:
        response = "I'm " + ctx.invoked_with[:-1] + "ing  " + ctx.author.name + " back!"

      gifsearch = (action(("anime" + ctx.invoked_with)))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Teal'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)

  #feeling
  @commands.cooldown(1, 5, commands.BucketType.member)
  @command(aliases=adjectives)
  async def sad(self, ctx, *, member: discord.Member = None):
    await ctx.message.delete()
    if member == None:
      if ctx.invoked_with in actionsdef:
        response = ctx.author.name + " is " + actionsdef[
          ctx.invoked_with] + "!"
      else:
        response = ctx.author.name + " is feeling " + ctx.invoked_with + "!"
    else:
      response = ctx.author.name + " just said " + member.name + " is " + ctx.invoked_with + "!"

    gifsearch = (action(("anime" + ctx.invoked_with)))
    giflink = RandomGif(gifsearch)
    gif = giflink.replace("'", ' ').replace(",", ' ')

    embed = discord.Embed(title=response, color=colord['Teal'])
    embed.set_image(url=gif)
    await ctx.send(embed=embed)
    print(gif)

    if "Izumi" in response:
      taction = random.choice(['happy', 'sorry'])
      response = f"Yeah, and I'm super {taction}!"
      gifsearch = (action(("anime" + taction)))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Teal'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      print('a')
      self.bot.command_ready.ready_up("action")


async def setup(bot):
  await bot.add_cog(Action(bot))
