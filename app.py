import os

try:
    import discord, datetime
    from discord import app_commands
    from config import Config
except:
    os.system("pip install -r importModules.txt")


class PlugS_Bot(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        await app.sync()
        print(f"{self.user} 에 로그인하였습니다!")


client = PlugS_Bot(intents=discord.Intents.all())
app = app_commands.CommandTree(client)


@client.event
async def on_member_join(self, member):
    created_at = member.created_at.strftime("%Y년 %m월 %d일 %p %I:%M")
    joined_at = member.joined_at.strftime("%Y년 %m월 %d일 %p %I:%M")
    await self.client.get_guild(Config.guild_id).get_channel(Config.join_channel_id).send(
        embed = discord.Embed(title=f"{member.name}님 께서 입장 했어요", color=0x3c9bff)
        .set_thumbnail(url=member.avatar.url)
        .add_field(name="**유저**", value=f"**{member.mention} ({member.name})**", inline=False)
        .add_field(name="**서버에 입장한 시간**", value=f"**{joined_at.replace('AM', '오전').replace('PM', '오후')}**", inline=False)
        .add_field(name="**계정 생성일**", value=f"**{created_at.replace('AM', '오전').replace('PM', '오후')}**", inline=False)
    )


@client.event
async def on_member_remove(self, member):
    created_at = member.created_at.strftime("%Y년 %m월 %d일 %p %I:%M")
    leave_at = datetime.datetime.now().strftime("%Y년 %m월 %d일 %p %I:%M")
    joined_at = member.joined_at.strftime("%Y년 %m월 %d일 %p %I:%M")
    await self.client.get_guild(Config.guild_id).get_channel(Config.leave_channel_id).send(
        embed = discord.Embed(title=f"{member.name}님 께서 퇴장 했어요", color=0xff5a5a)
        .set_thumbnail(url=member.avatar.url)
        .add_field(name="**유저**", value=f"**{member.mention} ({member.name})**", inline=False)
        .add_field(name="**서버에 퇴장한 시간**", value=f"**{leave_at.replace('AM', '오전').replace('PM', '오후')}**", inline=False)
        .add_field(name="**서버에 입장한 시간**", value=f"**{joined_at.replace('AM', '오전').replace('PM', '오후')}**", inline=False)
        .add_field(name="**계정 생성일**", value=f"**{created_at.replace('AM', '오전').replace('PM', '오후')}**", inline=False)
    )


client.run(Config.bot_token)