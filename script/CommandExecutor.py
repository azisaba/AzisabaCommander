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
import copy
        

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
            
            # send
            self.loop.create_task(message.channel.send(embed=embed))
        elif args[0] == 'search':
            # option
            return
        elif args[0] in self.commandMap.keys():
            command = self.commandMap[args[0]]
            # workspace
            if not command.workspace == None:
                workspace = command.workspace
                # exist
                if not os.path.exists(workspace):
                    # stop running
                    self.loop.create_task(message.channel.send(':boom:エラー: 指定したworkspaceが見つかりません'))
                    return
                # move
                os.chdir(workspace)
                # check
                print('change workspace. path: {0}'.format(str(os.getcwd())))            

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
                # loop
                for cmdOption in command.option[option]:
                    runCommand = copy.copy(command.base_command).replace("%OPTION%", cmdOption)
                    print("label: {0} Option: {1} Command: {2}".format(command.label, cmdOption, runCommand))
                    self.excuteCommand(message=message,command=runCommand)


            else:
                runCommand = copy.copy(command.base_command)
                print("label: {0} Option: {1} Command: {2}".format(command.label, 'None', runCommand))
                self.excuteCommand(message=message,command=runCommand)
            

        else:
            return

    def excuteCommand(self,message,command):
        # send typing
        self.loop.create_task(message.channel.trigger_typing())
        # run
        proc = subprocess.run(command.split(), stdout=PIPE, stderr=PIPE, text=True)
            
        ## feedback
        print("result: \n{0}".format(str(proc.stdout)))
        print("error: \n{0}".format(str(proc.stderr)))
        # discord
        embed = discord.Embed(title=":white_check_mark: コマンドを実行しました",description='Command: **{0}**'.format(message.content),color=discord.Colour.green())
        embed.add_field(name='Result',value="```\n{0}\n```".format(str(proc.stdout)),inline=False)
        embed.add_field(name='Error',value="```\n{0}\n```".format(str(proc.stderr)),inline=False)
        embed.set_author(name=message.author.name,icon_url=message.author.avatar_url)
        self.loop.create_task(message.channel.send(embed=embed))