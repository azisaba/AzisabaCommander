# -*- coding: utf-8 -*-
########################
#   Project: AzisabaCommander
#   Author: testusuke
#   Date: 2020/2/22
########################

import os
import yaml
from pathlib import Path

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
                self.guild = obl['guild']
                self.channel = obj['channel']
                self.prefix = obj['prefix']
                # command loader
                
        except Exception as e:
            traceback.print_exc()

        pass

