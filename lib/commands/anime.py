
from random import randrange
import asyncio

from jikanpy import AioJikan
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
from discord import Member
from replit import db
import nekos
import random
from discord import Embed,File
from lib.util.colors import colord
from lib.util.reactions import reactions

from lib.util.funtions import action
from lib.util.funtions import RandomGif
from lib.util.funtions import addlog
from lib.util.animeinfo import animesearch
from lib.util.animeinfo import allgenres
from lib.bot.__init__ import botname, botnick

class Anime(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.cancelled = False

      
    @command(aliases = ['animesearch', 'asearch'])
    async def anime(self, ctx, *, search):
      await ctx.message.delete()
      async with AioJikan() as aio_jikan:
        info = await aio_jikan.search(search_type='anime', query=search)
      anime = info['data'][0]
      print(anime)
      
      if len(anime['synopsis']) > 750:
        synopsis = (anime['synopsis'][:750] + '..') 
      else:
        synopsis = anime['synopsis']
      
      embed = discord.Embed(title = f"**{anime['titles'][0]['title']}**", color = colord['Pink'])
      embed.set_image(url=anime['images']['jpg']['large_image_url'])
      embed.add_field(name = 'Descrption', value = synopsis, inline = True)
      embed.add_field(name = 'Score:', value = str(anime['score']))
      embed.add_field(name = 'Type:', value = 'Anime', inline = True)
      embed.add_field(name = 'Episodes:', value = anime['episodes'])
      embed.add_field(name = 'Rating:', value = anime['rating'])
      embed.add_field(name = 'Members:', value = str(anime['members']))
      embed.add_field(name = 'Read More:', value = anime['url'])
      embed.set_footer(icon_url=ctx.author.avatar.url,text=f'Requested anime by {ctx.author.name}.')
      await ctx.send(embed = embed)
      
      addlog(ctx, f"Got MAL info about {anime['title']}.")
    @command(aliases = ['charsearch', 'char'])
    async def character(self, ctx, *, search):
      await ctx.message.delete()
      async with AioJikan() as aio_jikan:
        info = await aio_jikan.search(search_type='character', query=search)

      char = info['data'][0]

      x = 0
      if not char['anime'] == None:
        embed = discord.Embed(title = f"**{char['name']}**", color = colord['Pink'])
        embed.set_image(url=char['images']['jpg']['image_url'])
        embed.add_field(name = 'From:', value = char['anime'][0]['name'], inline = True)
        embed.add_field(name = 'Read More:', value = char['url'], inline = False)
        embed.set_footer(icon_url=ctx.author.avatar.url,text=f'Requested character by {ctx.author.name}.')
      else:
        while char['anime'] == None:
          x += 1
          char = info['data'][x]
          embed = discord.Embed(title = f"**{char['name']}**", color = colord['Pink'])
          embed.set_image(url=char['images']['jpg']['image_url'])
          embed.add_field(name = 'From:', value = char['anime'][0]['name'], inline = True)
          embed.add_field(name = 'Read More:', value = char['url'], inline = False)
          embed.set_footer(icon_url=ctx.author.avatar.url,text=f'Requested character by {ctx.author.name}.')
      print(char['name'])
      print(char['url'])
      await ctx.send(embed = embed)
      addlog(ctx, f"Got MAL info about {char['name']}.")


    @command(aliases = ['genre'])
    async def findanime(self, ctx, *, search):
      await ctx.message.delete()
      if search.lower() in allgenres:
        async with AioJikan() as aio_jikan:
          genre = await aio_jikan.genre(type = "anime", filter='genres')
          print(genre)
          char = genre['data'][randrange(int(len(genre['data'])))]

        async with AioJikan() as aio_jikan:
          info = await aio_jikan.search(search_type='anime', query='Action', parameters={'genre': allgenres[search.lower()]})
          print(info)
          anime = info['data'][0]
          embed = discord.Embed(title = f"**{anime['title']}**", color = colord['Pink'])
          embed.set_image(url=anime['images']['jpg']['image_url'])
          embed.add_field(name = '**Descrption:**', value = anime['synopsis'], inline = True)
          embed.add_field(name = '**Score:**', value = anime['score'])
          embed.add_field(name = '**Type:**', value = anime['type'], inline = True)
          embed.add_field(name = '**Episodes:**', value = anime['episodes'])
          embed.add_field(name = '**Rating:**', value = anime['rated'], inline = True)
          embed.add_field(name = '**Members:**', value = str(anime['members']))
          embed.add_field(name = '**Read More:**', value = anime['url'], inline = True)
          embed.set_footer(icon_url=ctx.author.avatar.url,text=f'Random Result for {search} genre for {ctx.author.name}.')
      else:
        embed = discord.Embed(title = "**That's not a valid genre.**", color = colord['Pink'])
      await ctx.send(embed = embed)
      addlog(ctx, f"Got MAL info about {anime['title']}.")

    @command()
    async def mal(self, ctx, *, search):
      await ctx.message.delete()
      
      async with AioJikan() as aio_jikan:
        aperson = await aio_jikan.users(username=search)
        person = aperson['data']
      
      '''     
      favanime = []
      favchar = []

      for item in person['favorites']['anime']:
        favanime.append(item['name'])
  
      for item in person['favorites']['characters']:
        favchar.append(item['name'])

      favanime = "\n".join(favanime)
      favchar = "\n".join(favchar)
  
      print(favanime)

      '''
      embed = discord.Embed(title = f"**{person['username']}'s Profile:**", color = colord['Pink'])
      embed.set_image(url=person['images']['jpg']['image_url'])
      '''
      embed.add_field(name = '**Days Watched:**', value = person['anime_stats']['days_watched'], inline = True)
      embed.add_field(name = '**Completed Anime:**', value = person['anime_stats']['completed'])

      embed.add_field(name = '**Favorite Anime:**', value = favanime)
      embed.add_field(name = '**Favorite Characters:**', value = favchar, inline = True)
      '''
      j = [character for character in (person['joined'][:10]) if character != '-']
      joindate = f"{''.join(j[4:6])}/{''.join(j[6:8])}/{''.join(j[0:4])}"
      
      print(joindate)
      embed.add_field(name = '**Date Joined:**', value = joindate, inline = True)
      embed.add_field(name = '**Read More:**', value = person['url'], inline = True)
      embed.set_footer(icon_url=ctx.author.avatar.url,text=f'Requested MAL User for {ctx.author.name}.')
 
      await ctx.send(embed = embed)
      addlog(ctx, f"Got MAL info about {person['username']}.")



    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("anime")

async def setup(bot):
    await bot.add_cog(Anime(bot))

