# -*- coding: utf-8 -*-
########################
#   Project: AzisabaCommander
#   Author: testusuke
#   Date: 2020/2/22
########################

import sys
import os
import discord
import ConfigLoader

####################
# Config Loader 
####################
path = sys.argv[1]
cl = ConfigLoader.ConfigLoader(path)
# discord token
token = ''
# command prefix
prefix = ''

####################
# Discord
####################
# build
client = discord.Client()

# events

@client.event
async def on_ready():
    print('Login: success!')

@client.event
async def on_message(message):
    # bot
    if message.author.bot:
        return
    # guild
    if not message.guild.id == guild_id:
        return
    # channel
    if not message.channel.id == channel_id:
        return
    # check prefix
    if not message.content[0] == prefix:
        return
    
    # get command label
    args = message.content.split()
    print(str(args))
    
    
    
        

client.run(token)
print('launch!')