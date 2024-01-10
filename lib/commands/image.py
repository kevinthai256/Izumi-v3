
from discord.ext.commands import Cog
from discord.ext.commands import command
import discord
from discord.ext import commands
from lib.util.colors import colord
from lib.util.funtions import action
from lib.util.funtions import RandomGif





#image commands

class Image(Cog):
    def __init__(self,bot):
        self.bot = bot


#GIF
    @command(aliases=['gif'])
    async def g(self, ctx, *, search=None):
      if search == None:
        search = "gif"

      gifsearch = (action((search)))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(color=colord['Yellow'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)


#Anime GIF
    @command(aliases=['animegif', 'ag'])
    async def a(self, ctx, *, search=None):
      if search == None:
        gifsearch = (action("anime"))
      else:
        gifsearch = (action(("anime" + search)))

      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')
      embed = discord.Embed(color=colord['Yellow'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)

#displays image
    @commands.has_permissions(manage_messages=True)
    @command(aliases=['image'])
    async def img(self, ctx, *, link):
  
      embed = discord.Embed(color=colord['White'])
      embed.set_image(url=link)

      await ctx.message.delete()
      await ctx.send(embed=embed)


    #Shows meme
    @command(aliases=['meme'])
    async def m(self, ctx, *, member: discord.Member = None):
      await ctx.message.delete()

      if member == None:
	      response = f"Here's a meme for you {ctx.author.name}!"
      else:
	      response = ctx.author.name + " sent a meme to " + member.name + "!"

      gifsearch = (action(('meme')))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Purple'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)      

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("image")

async def setup(bot):
    await bot.add_cog(Image(bot))