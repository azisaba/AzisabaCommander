# -*- coding: utf-8 -*-
########################
#   Project: AzisabaCommander
#   Author: testusuke
#   Class: Command
#   Date: 2020/2/23
########################

import dataclasses

@dataclasses.dataclass
class Command:
    label: str
    base_command: str
    has_option: bool
    option: dict