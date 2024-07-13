import discord
import dotenv

from server import server_thread

dotenv.load_dotenv()

# Discord Botのトークンをセットします（前述で取得したTokenを入れてください）
TOKEN = os.environ.get("TOKEN")

# Intentsを設定します（ボイスチャンネルの状態更新を受け取るために必要です）
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

# Clientを作成します
client = discord.Client(intents=intents)

@client.event
async def on_voice_state_update(member, before, after):
    # ユーザーがボイスチャンネルに参加した場合
    if before.channel is None and after.channel is not None:
        # ボイスチャンネルに最初の人が入ったときのみ通知します
        guild = member.guild
        channel = discord.utils.get(guild.channels, name='一般')  # 通知を送るチャンネル名を指定します
        if channel:
            await channel.send(f'先生！{member.display_name} が通話を始めましたよ！')

# Koyeb用　サーバー立ち上げ
server_theread()
client.run(TOKEN)
