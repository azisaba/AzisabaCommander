# -*- coding: utf-8 -*-
########################
#   Project: AzisabaCommander
#   Author: testusuke
#   Class: ConfigLoader
#   Date: 2020/2/22
########################

import os
import yaml
from pathlib import Path
import traceback
import Command

class ConfigLoader:

    def __init__(self,path):
        self.path = Path(os.path.abspath(path))
        print("Path: {0}".format(str(self.path)))
        # exist
        if not self.path.exists:
            raise Exception("file not found.")

        try:
            with open(self.path) as file:
                # PyYaml Setting
                yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                    lambda loader, node: OrderedDict(loader.construct_pairs(node)))
                obj = yaml.load(file)
                print(obj)
                # insert
                self.token = obj['token']
                self.guild = obj['guild']
                self.channel = obj['channel']
                self.prefix = obj['prefix']
                # command loader
                # init map
                self.commandMap = dict()
                for key in obj['command'].keys():
                    base_command = obj['command'][key]['base-command']
                    print(base_command)
                    #exist
                    command = None
                    if 'option' in obj['command'][key]:
                        # init list
                        option = []
                        # load options
                        for value in obj['command'][key]['option']:
                            option.append(str(value))
                            print(value)
                        command = Command.Command(label=key,base_command=base_command,has_option=True,option=option)
                    else:
                        command = Command.Command(label=key,base_command=base_command,has_option=False,option=None)
                    
                    # insert map
                    self.commandMap[key] = command
        except Exception as e:
            traceback.print_exc()

