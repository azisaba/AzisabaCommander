# -*- coding: utf-8 -*-
########################
#   Project: AzisabaCommander
#   Author: testusuke
#   Class: CommandExcutor
#   Date: 2020/2/23
########################

import os
import discord
from discord import Embed

class CommandExecutor:
    def __init__(self,client,**commandMap,prefix):
        print('CommandExecutor: init')
        self.client = client
        self.commandMap = commandMap
        self.prefix = prefix

    def onCommand(self,message,*args):
        
        if args[0] == 'help':
            embed = Embed(title='Help!',color=discord.Colour.red)
            embed.add_field(title='Commands:')
            embed.add_field(value='{0}help <- Helpの表示'.format(self.prefix))
            embed.add_field(value='{0}search [option] [file_path] [key_word]<- ファイル内の文字列検索'.format(self.prefix))
            embed.add_field(value='option: natural <-そのまま ignore <-小・大文字無視 and <-And検索 or <-Or検索')
            embed.add_field(value='file_path: ファイルパス(相対パスOK)')
            embed.add_field(value='{0}start [option] <- start server'.format(self.prefix))
            embed.add_field(value='{0}stop [option] <- stop server'.format(self.prefix))
            #embed.add_field(value='{0}'.format(self.prefix))
            embed.add_field(value='Author: testusuke')
            # send
            message.channel.send(embed=embed)
        elif args[0] == 'search':
            # option
        elif args[0] in commandMap:
