from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions, has_role
import discord
from discord import Member
from discord import Embed,File
from typing import Optional
from random import choice
from asyncio import TimeoutError, sleep
from lib.util.convert_time import convert

import discord
from discord.ext import commands
import random
from lib.util.colors import colord


from lib.util.jokes import jokes
from lib.util.jokes import puns

from lib.util.yes_or_no import yes_or_no
from lib.util.general_questions import questions
from lib.util.WYR_Questions import wyrq

from lib.util.functions import action, RandomGif, boldText, RandomChoice, RandomChoice2

import os
from dotenv import load_dotenv
load_dotenv()


#fun commands

class Fun(Cog):
    def __init__(self,bot):
        self.bot = bot
        

#8ball
    @command(name="_8ball", aliases=["8b"])
    async def _8ball(self, ctx, *, question):

        response = (f"Question: {question}\nAnswer: {(random.choice(yes_or_no))}")

        embed = discord.Embed(title="8 ball has decided..",
                          description=response,
                          color=colord['Purple'])
        embed.set_thumbnail(
        url=
        'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/8-Ball_Pool.svg/1024px-8-Ball_Pool.svg.png')
        await ctx.send(embed=embed)
    #pick
    @command(name="choose", aliases = ['pick', 'random'])
    async def choose(self, ctx, *, list):
      starter = random.choice(['Personally, I prefer', "I'd choose", 'The only right choice would be'])
      response = f"{starter} {RandomChoice2(list)}"

      embed = discord.Embed(title=response, color=colord['Purple'])

      await ctx.send(embed=embed)


#funny stuff
    @command(name="jokes", aliases=['joke', 'pun', 'badpun'])
    async def jokes(self, ctx):
        if ctx.invoked_with == 'pun' or ctx.invoked_with == 'badpun':
                response = f"Here's a random pun:\n{RandomChoice(puns)}"
        else:
            response = f"Here's a random joke:\n{RandomChoice(jokes)}"

        embed = discord.Embed(title=response, color=colord['Purple'])

        await ctx.send(embed=embed)


    @command(name="repeat", aliases = [])
    async def repeat(self, ctx, *, message):
      response = message

      embed = discord.Embed(title=response, color=colord['Orange'])

      await ctx.send(embed=embed)
    
    # AI integration with Gemini
    @command(name="ai", aliases=["i"])
    async def gemini(self, ctx, *, input):
        
        app_key = os.environ["GEMINI_API_KEY"]

        # Initialize the Gemini client
        client = genai.Client(api_key=app_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=input
        )
        reply = (f"Input: {input}\nAnswer: {response.text}")

        embed = discord.Embed(title="Result from Gemini",
                          description=reply,
                          color=colord['Purple'])
        embed.set_thumbnail(
        url=
        'https://registry.npmmirror.com/@lobehub/icons-static-png/latest/files/dark/gemini-color.png')
        await ctx.send(embed=embed)
  
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("fun")

async def setup(bot):
    await bot.add_cog(Fun(bot))