from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands import Bot, guild_only
from discord.ext import commands
import discord
from lib.util.cmd import version
from lib.util.functions import boldText
from lib.util.cmd import seperator
from lib.util.cmd import log
from lib.util.reactions import reactions
from lib.util.colors import colord



class Mod(Cog):
    def __init__(self,bot):
        self.bot = bot
          
#mod commands



#log
    @command(aliases = ['log'])
    async def updates(self, ctx):
  
      response = log
	
      embed = discord.Embed(title=f'Version: {version}', description = response, color=colord['Blue'])

      await ctx.send(embed=embed)


#clear
    @command(aliases=['clear', 'purge', 'delete'])
    @commands.has_permissions(manage_messages=True) 
    async def c(self, ctx, amount=1):
      await ctx.channel.purge(limit=amount + 1)
      
  
    @command(aliases=['announce', 'an'])
    @commands.has_permissions(manage_messages=True) 
    async def embed(self, ctx, ttitle, *, desc):
      await ctx.channel.purge(limit=1)
      embed = discord.Embed(title = ttitle, color = colord['White'], description = desc)
      await ctx.send(embed=embed)

    @command()
    @commands.has_permissions(manage_messages=True) 
    async def mute(self, ctx, member: discord.Member):

      newmuted = int(member.id)
      muted = (newmuted)

      #update_muted(muted)

      embed = discord.Embed(title = f'{member.name} has been muted.', color = colord['White'])
      await ctx.send(embed=embed)

    @command()
    @commands.has_permissions(manage_messages=True) 
    async def unmute(self, ctx, member: discord.Member):

      newmuted = int(member.id)
      muted = (newmuted)

      #remove_muted(muted)

      embed = discord.Embed(title = f'{member.name} has been unmuted.', color = colord['White'])
      await ctx.send(embed=embed)

    @command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
      if reason == None:
        reason = 'N/A'
      await ctx.guild.kick(member)
      await ctx.send(boldText(f'{member} has been kicked. | *{reason}*'))

    @command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
      if reason == None:
        reason = 'N/A'
      await ctx.guild.ban(member)
      await ctx.send(boldText(f'{member} has been banned. | *{reason}*'))

    @command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, member: discord.User):

      await ctx.guild.unban(member)
      await ctx.send(f'{member} was unbanned.')
      return
    
    
    @command()
    @commands.has_permissions(manage_messages=True) 
    async def poll(self, ctx, ttitle, *, options):
      await ctx.channel.purge(limit=1)
      roptions = options.split(' ')
      embed = discord.Embed(title = ttitle, color = colord['White'])
      print(roptions)
      for x in range(0, len(roptions)):
        pos = str(roptions.index(roptions[x]))
        embed.add_field(name = f"{roptions[x]} {reactions[pos]}", value = seperator, inline = False)
      msg = await ctx.send(embed=embed)
      for x in range(0, len(roptions)):
        emoji = reactions[str(x)]
        await msg.add_reaction(emoji)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("mod")
    

async def setup(bot):
    await bot.add_cog(Mod(bot))


