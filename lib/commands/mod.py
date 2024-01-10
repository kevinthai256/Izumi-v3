from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands
import discord
from lib.util.cmd import version
from lib.util.funtions import boldText
from lib.util.funtions import update_muted
from lib.util.funtions import remove_muted
from lib.util.funtions import update_user
from lib.util.funtions import update_xp
from lib.util.funtions import addlog
from lib.util.cmd import seperator
from lib.util.cmd import log
from lib.util.reactions import reactions
from lib.util.colors import colord
from replit import db
import math
from random import choice as choice



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
      addlog(ctx, 'Log info.')


#clear
    @command(aliases=['clear', 'purge', 'delete'])
    @commands.has_permissions(manage_messages=True) 
    async def c(self, ctx, amount=1):
      await ctx.message.delete()
      await ctx.channel.purge(limit=amount)
      if amount > 1:
        addlog(ctx, f'Cleared {amount} messages.')
      else:
        addlog(ctx, f'Cleared {amount} message.')
    
    @command(aliases=['announce', 'an'])
    @commands.has_permissions(manage_messages=True) 
    async def embed(self, ctx, ttitle, *, desc=None):
      await ctx.message.delete()
      if desc == None:
        embed = discord.Embed(title = ttitle, color = colord['White'])
      else:
        embed = discord.Embed(title = ttitle, color = colord['White'], description = desc)
      await ctx.send(embed=embed)
      addlog(ctx, f'Announcment: Title: {ttitle}  Desc: {desc}')

    @command()
    @commands.has_permissions(manage_messages=True) 
    async def mute(self, ctx, member: discord.Member):

      newmuted = int(member.id)
      muted = (newmuted)

      update_muted(muted)

      embed = discord.Embed(title = f'{member.name} has been muted.', color = colord['White'])
      await ctx.message.delete()
      await ctx.send(embed=embed)
      addlog(ctx, f'Muting {member.name}.')

    @command()
    @commands.has_permissions(manage_messages=True) 
    async def unmute(self, ctx, member: discord.Member):

      newmuted = int(member.id)
      muted = (newmuted)

      remove_muted(muted)

      embed = discord.Embed(title = f'{member.name} has been unmuted.', color = colord['White'])
      await ctx.message.delete()
      await ctx.send(embed=embed)
      addlog(ctx, f'Unmuting {member.name}.')
    @command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
      if reason == None:
        reason = 'N/A'
      await ctx.guild.kick(member)
      await ctx.message.delete()
      await ctx.send(boldText(f'{member} has been kicked. | *{reason}*'))
      addlog(ctx, f'Kicking {member.name}.')

    @command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
      if reason == None:
        reason = 'N/A'
      await ctx.guild.ban(member)
      await ctx.message.delete()
      await ctx.send(boldText(f'{member} has been banned. | *{reason}*'))
      addlog(ctx, f'Banning {member.name}.')

    @command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, member: discord.User):

      await ctx.guild.unban(member)
      await ctx.message.delete()
      await ctx.send(f'{member} was unbanned.')
      return
      addlog(ctx, f'Unbanning {member.name}.')
    
    @command(aliases = ['rmemb','rmember'])
    @commands.has_permissions(ban_members = True)
    async def ranmember(self, ctx):
      memlist = []
      async for member in ctx.guild.fetch_members(limit=None):
        memlist.append(member.mention)
      await ctx.message.delete()
      embed = discord.Embed(title = "Random Member!",description=f"I chose: {choice(memlist)}!", color = colord['Blue'])
      await ctx.send(embed=embed)

    
    @command()
    @commands.has_permissions(manage_messages=True) 
    async def poll(self, ctx, ttitle, *, options):
      alloptions = ""
      await ctx.message.delete()
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
        alloptions = alloptions.join(f'{x}. {roptions[x]}')
        addlog(ctx, f'Poll: Title: {ttitle} Options: {alloptions}')

    @command()
    @commands.has_permissions(ban_members = True)
    async def lvl(self, ctx, member: discord.Member, lvl):
      await ctx.message.delete()
      userid = member.id
      axp = int(lvl)
      if userid not in db['users']:
        update_user(userid)
        update_xp(axp)
      
      userindex = db['users'].index(userid)
      userxp = db['xp'][userindex]
      db['xp'][userindex] = math.floor(userxp + ((axp/0.23)*10))
      embed = discord.Embed(title = f"Level changed by {lvl} for {member.name}.", color = colord['Blue'])
      await ctx.send(embed=embed)
      addlog(ctx, f"Changed {member.name}'s level to {lvl}.")

    @command(aliases = ['role', 'addrole'])
    @commands.has_permissions(ban_members = True)
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        await ctx.message.delete()
        await user.add_roles(role)
        embed = discord.Embed(title = f'{ctx.author.name} has given {user.name} the "{role.name}" role!', color = colord['Blue'])
        await ctx.send(embed=embed)
        addlog(ctx, f'Gave {user.name} the {role.name} role.')

    @command(aliases = ['rrole'])
    @commands.has_permissions(ban_members = True)
    async def removerole(self, ctx, user: discord.Member, role: discord.Role):
        await ctx.message.delete()
        await user.remove_roles(role)
        embed = discord.Embed(title = f'{ctx.author.name} has removed the "{role.name}" role from "{user.name}!', color = colord['Blue'])
        await ctx.send(embed=embed)
        addlog(ctx, f'Removed the {role.name} role from {user.name}.')

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("mod")
    

async def setup(bot):
    await bot.add_cog(Mod(bot))


