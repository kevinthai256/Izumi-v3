
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands
import discord
from datetime import datetime
from lib.util.info import InfoTemplate
from lib.util.colors import colord
from lib.util.cmd import cmdinfo
from lib.util.cmd import acatagory
from lib.util.cmd import Updates
from lib.util.funtions import update_user
from lib.util.funtions import update_xp
from lib.util.actions import adjectives
from lib.util.actions import eactions
from lib.util.actions import actions
from replit import db
import math
from lib.util.images import nekoapi

class General(Cog):
    def __init__(self,bot):
        self.bot = bot
        bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

    @command(aliases=["cmd", "commands","help"])
    async def helpme(self, ctx, *,catagory='N/A'):
      prefix = '.'
      
      if 'N/A' in catagory:
        embed = discord.Embed(title="**Command Catagories: **",
	      color=colord['Blue'])
    
        embed.add_field(name=f'Prefix: {prefix}',
	      value='•-•-•-•-•-•-•-•-•',
	      inline=True)

        for item in acatagory.keys():
          embed.add_field(name = acatagory[item], value = f"cmd {item}", inline = False)
          
      else:
        for cat in cmdinfo:
          if catagory in cat.keys():        
            embed = discord.Embed(title=f'**{acatagory[catagory]}:**',
            color=colord['Blue'])
            for cmd in cat[catagory]:

              ccinfo=f"**{cmd['Syntax'].replace('`','')}**: `{cmd['bio']}`" 
              embed.add_field(name='•-•-•-•-•-•-•-•-•', value=ccinfo, inline=False)
          else:
            for cat in cmdinfo:
              for key in cat.keys():
                for cmd in cat[key]:
                  if catagory in cmd['Aliases']:

                    embed = discord.Embed(title=f"**{cmd['name']}:**")
                    ccinfo=f"**{cmd['Syntax'].replace('`','')}**\nAliases: `{cmd['Aliases']}`"
                    embed.add_field(name=cmd['bio'], value=ccinfo, inline=False)
                  else:
                    if catagory in (actions+eactions+adjectives):
                      embed = discord.Embed(title="**Action Commands:**")
                      ccinfo=f"**{catagory} <@user>**\nAliases: `see al command.`"
                      embed.add_field(name="Does something to another user!", value=ccinfo, inline=False)
                    
                      
        if embed == " ":
          embed = discord.Embed(title='**Catagory not found.**', color=colord['Blue'])
          embed.add_field(name='•-•-•-•-•-•-•-•-•', value="Maybe  try using cmd?", inline=True)
  

      embed.set_footer(icon_url=ctx.author.avatar.url, text=Updates)
      await ctx.send(embed=embed)
    

    @command(aliases = ['rank'])
    async def level(self, ctx, *, member: discord.Member = None):
      await ctx.message.delete()

      if member == None:
        member = ctx.author

      userid = member.id

      if not member.id in db['users']:
        update_user(userid)
        update_xp(50)
        
      userindex = db['users'].index(userid)
      userxp = db['xp'][userindex]
      level = math.floor(int(((userxp) * 0.23)/10))
      if max(db['xp']) == userxp:
        rank = 1
      else:
        rank = int(len(db['xp']))
        for item in db['xp']:
          if item < userxp:
            rank -= 1
      embed = discord.Embed(title = f"{member.name}'s Level:", color = colord['Blue'])
      embed.add_field(name = 'Rank: ', value = rank)
      embed.add_field(name = 'Total XP: ', value = userxp)
      embed.add_field(name = 'Level: ', value = level)
      embed.set_thumbnail(url = member.avatar.url)
      await ctx.send(embed=embed)

    @command()
    async def lb(self, ctx):
      await ctx.message.delete()
      seperator = '•-•-•-•-•-•-•-•-•'
      embed = discord.Embed(title ="Leaderboard:", color = discord.Color.blue())
      for x in range(0, 5):
        sxp = sorted(list(db['xp']))[::-1]
        
        userxp = sxp[x]
        xpindex = int(db['xp'].index(userxp))
        userid = list(db['users'])[xpindex]
        user = ctx.guild.get_member(userid)
        lvl = math.floor(int(((userxp) * 0.23)/10))
        embed.add_field(name = f"{x+1}. {user.name} (Level {lvl})", value = seperator, inline = False)
      await ctx.send(embed = embed)

    @command()
    @commands.has_permissions(ban_members = True)
    async def resetlvls(self, ctx):
      await ctx.message.delete()
      db['xp'] = []
      db['users'] = []
      embed = discord.Embed(title = "Levels Reset.", color = colord['Blue'])
      await ctx.send(embed=embed)


      

#shows info about user
    @command(aliases = ['whois', 'user'])
    async def info(self, ctx, *, member: discord.Member):
      x = datetime.now()

      pdthr = int(x.strftime("%H")) + 5

      if pdthr > 24:
        hr = str(pdthr - 7)
        ampm = 'pm'
      else:
        if pdthr > 12:
          hr = str(pdthr - 12)
          ampm = 'pm'
        else:
          if pdthr - 5 < 6:
           hr = str(pdthr)
           ampm = 'pm'
          else:
            hr = str(pdthr)
            ampm = 'am'

      minute = int(x.strftime("%M"))

      message = f'Today at: {hr}:{minute}{ampm}'

      seperator = '•-•-•-•-•-•-•-•-•'

      embed = discord.Embed(title=f"{member.name}'s Profile",
	                      color=colord['Blue'])
      created_at = member.created_at.strftime("%b %d, %Y")
      embed.add_field(name=f'{seperator}', value='\n**:**', inline=True)
      embed.add_field(name='ID', value=member.id, inline=False)
      embed.add_field(name='Joined Discord On:', value=created_at, inline=False)
      embed.add_field(name=":", value=f'{seperator}', inline=False)
      embed.set_thumbnail(url=member.avatar.url)
      embed.set_footer(icon_url=ctx.author.avatar.url,text=f'Requested by {ctx.author.name} | {message}')
      await ctx.message.delete()
      await ctx.send(embed=embed)

    @command(aliases = ['pfp', 'icon']) 
    async def av(self, ctx, *, member: discord.Member):
      embed = discord.Embed(title=f"{member.name}'s Avatar", color=colord['Blue'])
      embed.set_image(url=member.avatar.url)
      embed.set_footer(icon_url=ctx.author.avatar.url,text=f'Requested by {ctx.author.name}')
      await ctx.message.delete()
      await ctx.send(embed=embed)

      
    @command(aliases = ['welcome'])
    async def wc(self, ctx, *, member: discord.Member):
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

      embed = discord.Embed(title=f'Hi {member.name}!',descrpition=member.mention, color=colord['Blue'])

      seperator = '•-•-•-•-•-•-•-•-•'

      embed.add_field(name=f'{seperator}', value=InfoTemplate, inline=True)
      embed.add_field(name="**:**", value=f'{seperator}', inline=False)
      embed.set_thumbnail(url=member.avatar.url)
      embed.set_footer(icon_url=member.avatar.url,  text=f'Welcome to the server! • {message}')
      await ctx.send(embed=embed)
      
#Shows actionlist
    @command(aliases=["termlist", "al", "actionlist", 'actions', 'terms'])
    async def tl(self, ctx):
      allacts = actions + eactions + adjectives
      embed = discord.Embed(title='Action List:', color=colord['Teal'])
      embed.add_field(name='Avaliable Terms', value=allacts)

      await ctx.send(embed=embed)

    @command(aliases=["nsfwterms"])
    async def nsfwc(self, ctx):
      allacts = nekoapi
      embed = discord.Embed(title='NSFW Action List:', color=colord['Teal'])
      embed.add_field(name='Avaliable Terms', value=allacts)

      await ctx.send(embed=embed)
    

    @command(name="cmd giveaway", aliases=["ghelp", "givhelp", "givehelp"])
    async def help_user(self, ctx):
        embed = discord.Embed(title="Giveaway setup Help",
                      description="Setup Your giveaway in some simple commands",
                      color=ctx.author.color)
        embed.add_field(name="Create Giveaway", value="Create a giveaway by using the .giveaway command. You can also .giftcr.The bot will ask some simple questions to host your giveaway.")
        embed.add_field(name="Reroll Giveaway", value="Reroll a giveaway again by using the !gifreroll command. Additionally you can also use commands like .gftroll or .giftrrl. The bot will ask some simple questions to host your giveaway.")
        embed.add_field(name="Cancel Giveaway", value="Delete a giveaway by using the .giftdel command. Additionally you can also use commands like .gftdel or .gifdel. The bot will ask some simple questions to host your giveaway.")
        await ctx.send(embed=embed)

    @command(name="math", aliases = ['calculate','solve'])
    async def math(self, ctx, *, message):
      
      response = f"{message} = {eval(message)}!"

      embed = discord.Embed(title=response, color=colord['Orange'])

      await ctx.send(embed=embed)
      return

    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
          self.bot.command_ready.ready_up("general")
          print("ready for general")

async def setup(bot):
    await bot.add_cog(General(bot))
    print("loaded general")


