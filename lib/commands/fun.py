from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions, has_role
from discord.ext import commands
import discord
from discord import Member
from discord import Embed,File
from typing import Optional
from random import choice
from asyncio import TimeoutError, sleep
from lib.util.convert_time import convert
from random import randint
from io import BytesIO
import discord
from replit import db
import random
from lib.util.colors import colord

from lib.util.jokes import jokes
from lib.util.jokes import videos
from lib.util.jokes import puns

from lib.util.yes_or_no import yes_or_no
from lib.util.general_questions import questions
from lib.util.WYR_Questions import wyrq

from lib.util.funtions import ntinder
from lib.util.funtions import action
from lib.util.funtions import RandomGif
from lib.util.funtions import boldText
from lib.util.funtions import addlog
from lib.util.funtions import RandomChoice
from lib.util.funtions import RandomChoice2
from lib.util.funtions import update_tree
from PIL import Image,ImageDraw,ImageFont, ImageOps




#fun commands

class Fun(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="discord", aliases=[])
    @commands.has_permissions(ban_members = True)
    async def discordm(self, ctx, member: discord.Member = None,*,txt):
      if member == None:
        member = ctx.author
      print('a')
      img = Image.open("discordtemplate.png")
      asset = ctx.author.avatar(size=64)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      mask = Image.open('dmask.png')
      img.paste(pfp, (12,17))
      img.paste(mask, (12,17))
      d = ImageDraw.Draw(img)
      fnt = ImageFont.truetype("whitneymedium.otf", 20)
      tfnt = ImageFont.truetype("whitneysemibold.otf", 20)
      d.text((93, 21), member.nick, fill = (121,189,228), font=tfnt)
      d.text((93, 46), wrap(txt,570), fill = (220,210,201), font=fnt)
      img.save("discord.png","PNG")
      await ctx.send(file=File("discord.png"))
      
    @command(name="komi", aliases=["komimeme"])
    async def komi(self, ctx, *, text):
      img = Image.open("komi.png")
      d = ImageDraw.Draw(img)
      fnt = ImageFont.truetype("SF-UI-Display-Regular.otf", 24)
      d.text((101, 61), d.wrap(text, 250), fill = 000000, font=fnt)
      img.save("ekomi.png","PNG")
      await ctx.send(file=File("ekomi.png"))  
    
    @command(name="tinderedit", aliases=["tindere"])
    async def tinderedit(self, ctx, age: int=randint(0,99),*,txt):
      temp = db['tdict']
      temp[str(ctx.author.id)] = {"age":str(age),"bio":txt}

      
      img = Image.open("tinderprofilew.png")
      asset = ctx.author.avatar(size=512)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      pfp = pfp.resize((700,700))
      img.paste(pfp,(0,111))
      d = ImageDraw.Draw(img)
      age = temp[str(ctx.author.id)]['age']
      bio = temp[str(ctx.author.id)]['bio']
      tfnt = ImageFont.truetype("SF-UI-Display-Regular.otf", 40)
      fnt = ImageFont.truetype("SF-UI-Display-Regular.otf", 24)
      d.text((28, 847), f"{ctx.author.name} , {age}", fill = (142,142,142), font=tfnt)
      d.text((28, 956), d.wrap(bio,650), fill = (142,142,142), font=fnt)
      img.save("tinder.png","PNG")
      embed = discord.Embed(title="Tinder profile has been created! Here's a preview:",
	                      color=colord['Purple'])
      await ctx.send(embed=embed)
      await ctx.send(file=File("tinder.png"))


    @command(name="tinder", aliases=["tinderprof"])
    async def tinder(self, ctx, *, member: discord.Member = None):
      if member == None:
        user = ctx.author
      else:
        user = member
      
      img = Image.open("tinderprofilew.png")
      asset = user.avatar(size=512)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      pfp = pfp.resize((700,700))
      img.paste(pfp,(0,111))
      d = ImageDraw.Draw(img)
      tfnt = ImageFont.truetype("SF-UI-Display-Regular.otf", 40)
      fnt = ImageFont.truetype("SF-UI-Display-Regular.otf", 24)
      tdict=db['tdict']
      age = tdict[str(user.id)]['age']
      bio = tdict[str(user.id)]['bio']
      if not age == None:
        d.text((28, 847), f"{user.name}, {age}", fill = (142,142,142), font=tfnt)
        d.text((28, 956), d.wrap(bio,650), fill = (142,142,142), font=fnt)
        img.save("tinder.png","PNG")
        await ctx.send(file=File("tinder.png"))    
      else:
        embed = discord.Embed(title="Tinder profile hasn't been created!",
	                      description="(you can make one using `tinderedit`!)",
	                      color=colord['Purple'])

        await ctx.send(embed=embed)  

#8ball
    @command(name="_8ball", aliases=["8b", "8ball"])
    async def _8ball(self, ctx, *, question):

	    response = (f"Question: {question}\nAnswer: {(random.choice(yes_or_no))}")

	    embed = discord.Embed(title="8 ball has decided..",
	                      description=response,
	                      color=colord['Purple'])
	    embed.set_thumbnail(
	    url=
	    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/8-Ball_Pool.svg/1024px-8-Ball_Pool.svg.png')
	    await ctx.send(embed=embed)

#topic
    @command(name="qe", aliases=["question", "topic", "randomtopic"])
    async def _q(self, ctx):

	    response = str(RandomChoice(questions))

	    embed = discord.Embed(title=response, color=colord['Purple'])

	    await ctx.send(embed=embed)

    #say
    @command(name="say", aliases=["s"])
    async def say(self, ctx, *, search):
      await ctx.message.delete()

      response = f"{ctx.author.name} said '{search}'"
      gifsearch = (action((search)))

      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Purple'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)
      print(gif)

#wyr
    @command(name='wyr', aliases = [])
    async def wyr(self, ctx):

	    response = RandomChoice(wyrq)

	    embed = discord.Embed(title=response, color=colord['Purple'])

	    await ctx.send(embed=embed)

    #pick
    @command(name="choose", aliases = ['pick', 'random'])
    async def choose(self, ctx, *, list):
      starter = random.choice(['Personally, I prefer', "I'd choose", 'The only right choice would be'])
      response = f"{starter} {RandomChoice2(list)}"

      embed = discord.Embed(title=response, color=colord['Purple'])

      await ctx.send(embed=embed)


#funny stuff
    @command(name="video", aliases=['joke', 'pun', 'badpun'])
    async def video(self, ctx):
	    if ctx.invoked_with == 'video':
		    response = f"Here's a random video:\n<{random.choice(videos)}>"
	    else:
		    if ctx.invoked_with == 'pun' or ctx.invoked_with == 'badpun':
			    response = f"Here's a random pun:\n{RandomChoice(puns)}"
		    else:
			    if ctx.invoked_with == 'joke':
				    response = f"Here's a random joke:\n{RandomChoice(jokes)}"

	    embed = discord.Embed(title=response, color=colord['Purple'])

	    await ctx.send(embed=embed)

    @command(name="dice", aliases=['roll'])
    async def dice(self, ctx, *, number=6):

      response = random.randint(0,int(number))
      embed = discord.Embed(title=f"You rolled: `{response}`!",color=colord['Purple'])
      await ctx.send(embed=embed)



    @command(name="repeat", aliases = [])
    async def repeat(self, ctx, *, message):
      
      response = message

      embed = discord.Embed(title=response, color=colord['Orange'])

      await ctx.send(embed=embed)
      return

    #planttree
    @commands.cooldown(1,600,commands.BucketType.guild)
    @command(name="planttree", aliases = [])
    async def planttree(self, ctx):
      
      await ctx.message.delete()

      if "trees" in db.keys():
        totaltrees = db["trees"]
      else:
        db['trees'] = ["0"]
        totaltrees = db["trees"]

      newtree = int(random.choice(totaltrees)) + 1
      trees = (newtree)

      if "trees" in db.keys():
        db["trees"] = []

      update_tree(trees)
      

      response = f'A new tree was planted! There are now {trees} trees!'
      embed = discord.Embed(title=response, color=colord['Green'])
      await ctx.send(embed=embed)
      return

    @command(name="totaltree", aliases = ["trees","tree","totaltrees"])
    async def totaltree(self, ctx):
      totaltrees = db["trees"]
      trees = int(totaltrees[0])
      await ctx.message.delete()
      response = f'There are {trees} trees!'
      
      embed = discord.Embed(title=response, color=colord['Green'])
      await ctx.send(embed=embed)
      return
  
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("fun")

async def setup(bot):
    await bot.add_cog(Fun(bot))
  