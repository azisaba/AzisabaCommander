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
import Command
import asyncio
import subprocess
from subprocess import PIPE

        

class CommandExecutor:
    def __init__(self,client,commandMap,prefix):
        print('CommandExecutor: init')
        self.client = client
        self.commandMap = commandMap
        self.prefix = prefix
        self.loop = asyncio.get_event_loop()

    def onCommand(self,message,args):
        # args length
        if len(args) < 1:
            return

        if args[0] == 'help':
            descript = ""
            descript += "AzisabaCommander Discordからのコマンド実行を行います \n"
            embed = Embed(title='Help!',description=descript)
            #embed.add_field(name='Commands:',value=" ")
            #embed.add_field(,value='{0}help <- Helpの表示')
            #embed.add_field(value='{0}search [option] [file_path] [key_word]<- ファイル内の文字列検索'.format(self.prefix))
            #embed.add_field(value='option: natural <-そのまま ignore <-小・大文字無視 and <-And検索 or <-Or検索')
            #embed.add_field(value='file_path: ファイルパス(相対パスOK)')
            #embed.add_field(value='{0}start [option] <- start server'.format(self.prefix))
            #embed.add_field(value='{0}stop [option] <- stop server'.format(self.prefix))
            #embed.add_field(value='{0}'.format(self.prefix))
            #embed.add_field(value='Author: testusuke')

            # send
            self.loop.create_task(message.channel.send(embed=embed))
        elif args[0] == 'search':
            # option
            return
        elif args[0] in self.commandMap.keys():
            command = self.commandMap[args[0]]
            #print(command.label)
            if command.has_option == True:
                # len check
                if len(args) < 2:
                    self.loop.create_task(message.channel.send(':boom:エラー: Optionを指定してください'))
                    return
                # check options
                option = args[1]
                if not option in command.option:
                    self.loop.create_task(message.channel.send(':boom:エラー: そのようなOptionは存在しません'))
                    return
                runCommand = command.base_command.replace("%OPTION%", option)
                print("label: {0} Option: {1} Command: {2}".format(command.label, option, runCommand))
                print("running command....")

                # send typing
                self.loop.create_task(message.channel.trigger_typing())

                # run
                proc = subprocess.run(runCommand.split(), stdout=PIPE, stderr=PIPE, text=True)
                # feedback
                print("result: \n{0}".format(str(proc.stdout)))
                print("error: \n{0}".format(str(proc.stderr)))

                self.loop.create_task(message.channel.send(':white_check_mark:結果: コマンドを実行しました'))
                result_str = "**Result**\n```\n{0}\n```".format(str(proc.stdout))
                error_str = "**Error**\n```\n{0}\n```".format(str(proc.stderr))
                self.loop.create_task(message.channel.send(result_str))
                self.loop.create_task(message.channel.send(error_str))
            else:
                runCommand = command.base_command
                print("label: {0} Option: {1} Command: {2}".format(command.label, 'None', runCommand))
                print("running command....")
                
                # send typing
                self.loop.create_task(message.channel.trigger_typing())
                
                # run
                proc = subprocess.run(runCommand.split(), stdout=PIPE, stderr=PIPE, text=True)
                # feedback
                print("result: \n{0}".format(str(proc.stdout)))
                print("error: \n{0}".format(str(proc.stderr)))

                self.loop.create_task(message.channel.send(':white_check_mark:結果: コマンドを実行しました'))
                result_str = "**Result**\n```\n{0}\n```".format(str(proc.stdout))
                error_str = "**Error**\n```\n{0}\n```".format(str(proc.stderr))
                self.loop.create_task(message.channel.send(result_str))
                self.loop.create_task(message.channel.send(error_str))
        else:
            return

