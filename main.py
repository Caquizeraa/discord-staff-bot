import discord
import io
from discord.ext import commands
client = discord.Client()

token = 'TOKEN DO BOT AQUI'
prefix = 'PREFIXO AQUI'

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot online!\nID: {client.user.id}\nNome: {client.user}')

@client.event
async def on_message(message):
    file = io.open("badwords.txt", "r", encoding='utf-8')
    words = file.read().splitlines()
    for i in range(len(words)):
        if words[i] in message.content:
            await message.channel.send(f"Não seja tão ofensivo <@{message.author.id}>!")
            await message.delete()
            break
    await client.process_commands(message)

@client.command()
async def add(ctx, *, msg = None):
    file = io.open("badwords.txt", "r", encoding='utf-8')
    words = file.read().splitlines()
    added = False
    if ctx.author.guild_permissions.ban_members:
        if msg is None:
            await ctx.send('Nenhuma palavra foi adicionada!')
        else:
            for i in range(len(words)):
                if words[i] in msg:
                    added = True
                    break
            if added is False:
                with open('badwords.txt','a') as wordsfile:
                    wordsfile.write(f'\n{msg}')
                    await ctx.message.add_reaction("👍")
    else:
        await ctx.send('Você não tem permissão!')

client.run(token)