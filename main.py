import discord
import asyncio
from discord.client import _ClientEventTask
import requests
from random import randint
from flask import Flask
from threading import Thread
app = Flask('discord bot')


@app.route('/')
def hello_world():
    return 'beep boop'


def start_server():
    app.run(host='0.0.0.0', port=8080)


t = Thread(target=start_server)
t.start()

client = discord.Client()

//starts bot!
@client.event
async def on_ready():
    print('LOGGED IN:')
    print(client.user.name)
    print(client.user.id)
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format('438846142349049856'))
    print('------')


@client.event
async def on_ready():
    activity = discord.Game(name="discord.gg/qbcore", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")


client.run('UR TOKEN')
