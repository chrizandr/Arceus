import discord
import os
from keep_alive import keep_alive
from misc import fun_commands
from trainer_id import trainer_id_handler
from rarity import rarity_handler
from for_trade import trainer_ft_handler
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        fun_response = fun_commands(message)
        if fun_response is not None:
            await message.channel.send(fun_response)

        if message.content.startswith("!id"):
            response = trainer_id_handler(message)
            await message.channel.send(response)
        if message.content.startswith("!ft"):
            response = trainer_ft_handler(message)
            await message.channel.send(response)

        if message.content.startswith("!rarity"):
            response = rarity_handler(message)
            if type(response) is discord.embeds.Embed:
                await message.channel.send(embed=response)
            else:
                await message.channel.send(response)

    except discord.errors.HTTPException as e:
        print(e)


# keep_alive()
client.run(os.getenv('TOKEN'))
