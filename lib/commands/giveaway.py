
from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions, has_role
import discord
from discord import Member
from discord import Embed,File
from typing import Optional
from random import choice
from asyncio import TimeoutError, sleep
from lib.util.convert_time import convert
from lib.util.images import miyamura
from lib.util.colors import colord
from lib.util.funtions import addlog

class Giveaway(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.cancelled = False

    @command(name="givcr", aliases=["giveaway", "gcreate", "gcr"])
    @has_permissions(manage_guild=True)
    async def create_giveaway(self, ctx):
        #Ask Questions
        embed = Embed(title="Giveaway Time!!✨",
                      description="Time for a new Giveaway. Answer the following questions in 25 seconds each for the Giveaway",
                      color=ctx.author.color)
        await ctx.send(embed=embed)
        questions=["In Which channel do you want to host the giveaway?",
                   "For How long should the Giveaway be hosted ? type number followed (s|m|h|d)",
                   "What is the Prize?"]
        answers = []
        #Check Author
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        for i, question in enumerate(questions):
            embed = Embed(title=f"Question {i}",
                          description=question, color = colord['Green'])
            await ctx.send(embed=embed)
            try:
                message = await self.bot.wait_for('message', timeout=25, check=check)
            except TimeoutError:
                late = Embed(title=f"You didn't answer the question in time.", color = colord['Green'])
                await ctx.send(embed = late)
                return
            answers.append(message.content)
        #Check if Channel Id is valid
        try:
            channel_id = int(answers[0][2:-1])
        except:
            await ctx.send(f"The Channel provided was wrong. The channel should be {ctx.channel.mention}")
            return

        channel = self.bot.get_channel(channel_id)
        time = convert(answers[1])
        #Check if Time is valid
        if time == -1:
            formatw = Embed(title=f"The time format was wrong.", color = colord['Green'])
            await ctx.send(embed = formatw)
            return
        elif time == -2:
            number = Embed(title=f"The time was not a conventional number.", color = colord['Green'])
            await ctx.send(embed = number)
            return
        prize = answers[2]

        await ctx.send(f"Your giveaway will be hosted in {channel.mention} and will last for {answers[1]}")
        embed = Embed(title="Giveaway Time !!",
                    description=f"Win a {prize} today",
                    color = colord['Green'])
        embed.add_field(name="Hosted By:", value=ctx.author.mention)
        embed.set_footer(text=f"Giveway ends in {answers[1]} !")
        newMsg = await channel.send(embed=embed)
        await newMsg.add_reaction("🎉")
        addlog(ctx, f"Created a Giveaway: Prize: {prize} Host: {ctx.author}")
        #Check if Giveaway Cancelled
        self.cancelled = False
        await sleep(time)
        if not self.cancelled:
            myMsg = await channel.fetch_message(newMsg.id)
            users = await myMsg.reactions[0].users().flatten()
            users.pop(users.index(self.bot.user))
            #Check if User list is not empty
            if len(users) <= 0:
                emptyEmbed = Embed(title="GIVEAWAY ENDED",description=f"Win a {prize} today!", color = colord['Red'])
                emptyEmbed.add_field(name="Hosted By:", value=ctx.author.mention)
                emptyEmbed.set_footer(text="No one won the Giveaway.")
                await myMsg.edit(embed=emptyEmbed)
                return
              
            if len(users) > 0:
                winner = choice(users)
                winnerEmbed = Embed(title="GIVEAWAY ENDED",description=f"Win a {prize} today!",color = colord['Red'])
                winnerEmbed.add_field(name=f"Congratulations On Winning {prize}", value=winner.mention)
                winnerEmbed.set_image(url=choice(miyamura))
                await myMsg.edit(embed=winnerEmbed)
                return
                
    @command(name="givrrl", aliases=["givreroll", "givroll", "grr"])
    @has_permissions(manage_guild=True)
    async def giveaway_reroll(self, ctx, channel : discord.TextChannel, id_: int):
        try:
            msg = await channel.fetch_message(id_)
        except:
            await ctx.send("The channel or ID mentioned was incorrect")
        users = await msg.reactions[0].users().flatten()
        if len(users) <= 0:
            emptyEmbed = Embed(title="GIVEAWAY ENDED",
                                   description=f"Win a Prize today", color = colord['Red'])
            emptyEmbed.add_field(name="Hosted By:", value=ctx.author.mention)
            emptyEmbed.set_footer(text="No one won the Giveaway.")
            await msg.edit(embed=emptyEmbed)
            return
        if len(users) > 0:
            winner = choice(users)
            winnerEmbed = Embed(title="GIVEAWAY ENDED",
                                description=f"Win a Prize today",
                                color = colord['Red'])
            winnerEmbed.add_field(name=f"Congratulations On Winning Giveaway!", value=winner.mention)
            winnerEmbed.set_image(url=choice(miyamura))
            await msg.edit(embed=winnerEmbed)
            return

    @command(name="gdel", aliases=["givdel", "givedel", "gdl"])
    @has_permissions(manage_guild=True)
    async def giveaway_stop(self, ctx, channel : discord.TextChannel, id_: int):
        try:
            msg = await channel.fetch_message(id_)
            newEmbed = Embed(title="GIVEAWAY CANCELED", description="The giveaway has been cancelled!!", color = colord['Orange'])
            #Set Giveaway cancelled
            self.cancelled = True
            await msg.edit(embed=newEmbed) 
        except:
            embed = Embed(title="Failure!", description="Cannot cancel Giveaway")
            await ctx.send(emebed=embed)


    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("giveaway")

async def setup(bot):
    await bot.add_cog(Giveaway(bot))