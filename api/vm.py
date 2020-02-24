#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import payload
import json

def id(args, authenticated):
    url = "https://%s/rest/vcenter/vm" % (args.vcenter)
    vms = payload.get(authenticated, url)
    json_data = vms["value"]
    for vm in json_data:
        if vm.get("name") == args.vm_name:
            data = vm.get("vm")
            return data



