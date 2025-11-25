import discord
from discord.ext.commands import Cog, command
from random import randrange
import aiohttp
from lib.util.colors import colord
from lib.util.animeinfo import allgenres

class Anime(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cancelled = False
        self.base_url = "https://api.jikan.moe/v4"

    async def fetch_data(self, endpoint):
        """Helper method to fetch data from Jikan API v4"""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/{endpoint}") as response:
                if response.status == 200:
                    return await response.json()
                return None

    @command(aliases=['animesearch', 'asearch'])
    async def anime(self, ctx, *, search):
        await ctx.channel.purge(limit=1)

        # Search for anime using v4 API
        data = await self.fetch_data(f"anime?q={search}&limit=1")

        if not data or not data.get('data'):
            await ctx.send("No anime found with that search term.")
            return

        anime = data['data'][0]
        embed = discord.Embed(title=anime['title'], color=colord['Pink'])

        # v4 uses 'images' object instead of direct 'image_url'
        image_url = anime['images']['jpg']['large_image_url']
        embed.set_image(url=image_url)

        # v4 uses 'synopsis' directly
        synopsis = anime.get('synopsis', 'No synopsis')
        if synopsis and len(synopsis) > 1024:
            synopsis = synopsis[:1021] + "..."

        embed.add_field(name='Description', value=synopsis, inline=True)
        embed.add_field(name='Score', value=anime.get('score', 'N/A'), inline=True)
        embed.add_field(name='Type', value=anime.get('type', 'N/A'), inline=True)
        embed.add_field(name='Episodes', value=anime.get('episodes', 'N/A'), inline=True)
        embed.add_field(name='Rating', value=anime.get('rating', 'N/A'), inline=True)
        embed.add_field(name='Members', value=str(anime.get('members', 'N/A')), inline=True)
        embed.add_field(name='Read More', value=anime.get('url', 'N/A'), inline=True)
        embed.set_footer(icon_url=ctx.author.display_avatar.url,
                         text=f'Requested anime by {ctx.author.name}.')

        await ctx.send(embed=embed)

    @command(aliases=['charsearch', 'char'])
    async def character(self, ctx, *, search):
        await ctx.channel.purge(limit=1)

        # Search for character using v4 API
        data = await self.fetch_data(f"characters?q={search}&limit=1")

        if not data or not data.get('data'):
            await ctx.send("No character found with that search term.")
            return

        char = data['data'][0]
        embed = discord.Embed(title=char['name'], color=colord['Pink'])

        # v4 uses 'images' object
        image_url = char['images']['jpg']['image_url']
        embed.set_image(url=image_url)

        # Get character's full info to find anime appearances
        char_id = char['mal_id']
        char_full = await self.fetch_data(f"characters/{char_id}/full")

        if char_full and char_full.get('data', {}).get('anime'):
            anime_list = char_full['data']['anime']
            if anime_list:
                embed.add_field(name='From', value=anime_list[0]['anime']['title'], inline=True)

        embed.add_field(name='Read More', value=char['url'], inline=False)
        embed.set_footer(icon_url=ctx.author.display_avatar.url,
                         text=f'Requested character by {ctx.author.name}.')

        await ctx.send(embed=embed)

    @command(aliases=['genre'])
    async def findanime(self, ctx, *, search):
        await ctx.channel.purge(limit=1)

        if search not in allgenres:
            await ctx.send(f"Genre '{search}' not found.")
            return

        genre_id = allgenres[search]

        # Get anime by genre using v4 API
        data = await self.fetch_data(f"anime?genres={genre_id}&order_by=popularity&limit=25")

        if not data or not data.get('data'):
            await ctx.send("No anime found for this genre.")
            return

        # Pick a random anime from results
        anime = data['data'][randrange(len(data['data']))]

        embed = discord.Embed(title=anime['title'], color=colord['Pink'])

        image_url = anime['images']['jpg']['large_image_url']
        embed.set_image(url=image_url)

        synopsis = anime.get('synopsis', 'No synopsis')
        if synopsis and len(synopsis) > 1024:
            synopsis = synopsis[:1021] + "..."

        embed.add_field(name='Description', value=synopsis, inline=True)
        embed.add_field(name='Score', value=anime.get('score', 'N/A'))
        embed.add_field(name='Type', value=anime.get('type', 'N/A'), inline=True)
        embed.add_field(name='Episodes', value=anime.get('episodes', 'N/A'))
        embed.add_field(name='Rating', value=anime.get('rating', 'N/A'), inline=True)
        embed.add_field(name='Members', value=str(anime.get('members', 'N/A')))
        embed.add_field(name='Read More', value=anime.get('url', 'N/A'), inline=True)
        embed.set_footer(icon_url=ctx.author.display_avatar.url,
                         text=f'Random result for {search} genre requested by {ctx.author.name}.')

        await ctx.send(embed=embed)

    @command()
    async def mal(self, ctx, *, search):
        await ctx.channel.purge(limit=1)

        # Get user profile using v4 API
        data = await self.fetch_data(f"users/{search}/full")

        if not data or not data.get('data'):
            await ctx.send("User not found.")
            return

        user = data['data']

        # Get favorite anime names
        favanime = "\n".join([item['title'] for item in user['favorites']['anime']]) if user['favorites']['anime'] else "None"

        # Get favorite character names
        favchar = "\n".join([item['name'] for item in user['favorites']['characters']]) if user['favorites']['characters'] else "None"

        embed = discord.Embed(title=f"{user['username']}'s Profile:", color=colord['Pink'])
        embed.set_image(url=user['images']['jpg']['image_url'])
        embed.add_field(name='Days Watched', value=user['statistics']['anime']['days_watched'], inline=True)
        embed.add_field(name='Completed Anime', value=user['statistics']['anime']['completed'])
        embed.add_field(name='Planning to Watch', value=user['statistics']['anime']['plan_to_watch'], inline=True)

        # Truncate if too long for Discord embed field
        if len(favanime) > 1024:
            favanime = favanime[:1021] + "..."
        if len(favchar) > 1024:
            favchar = favchar[:1021] + "..."

        embed.add_field(name='Favorite Anime', value=favanime)
        embed.add_field(name='Favorite Characters', value=favchar, inline=True)
        embed.add_field(name='Read More', value=user['url'], inline=True)
        embed.set_footer(icon_url=ctx.author.display_avatar.url,
                         text=f'Requested MAL user by {ctx.author.name}.')

        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("anime")


async def setup(bot):
    await bot.add_cog(Anime(bot))