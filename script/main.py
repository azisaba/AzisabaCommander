# -*- coding: utf-8 -*-
########################
#   Project: AzisabaCommander
#   Author: testusuke
#   Class: Main
#   Date: 2020/2/22
########################

import sys
import os
import discord
import ConfigLoader
import CommandExecutor
import asyncio

####################
# Config Loader 
####################
path = sys.argv[1]
cl = ConfigLoader.ConfigLoader(path)
# discord setting
token = cl.token
prefix = cl.prefix
guild_id = cl.guild
channel_id = cl.channel
####################
# Discord
####################
# build
client = discord.Client()

# CommandExecutor
ce = CommandExecutor.CommandExecutor(client,cl.commandMap,prefix)

# events
@client.event
async def on_ready():
    print('Login: success!')
    # send message
    ch = client.get_guild(int(guild_id)).get_channel(int(channel_id))
    await ch.send(':wink: **Launched AzisabaCommander!**')

@client.event
async def on_message(message):
    # bot
    if message.author.bot:
        return
    # guild
    if not message.guild.id == int(guild_id):
        return
    # channel
    if not message.channel.id == int(channel_id):
        return
    # check prefix
    if not message.content[0] == prefix:
        return
    
    msg = message.content[1:]
    # get command label
    args = msg.split()
    print(str(args))
    # 受け渡し
    ce.onCommand(message,args)
    

# run
client.run(token)