#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import payload


def get(args, authenticated):
    url = "https://%s/rest/vcenter/vm" % args.host
    vms = payload.get(authenticated, url)
    json_data = vms["value"]
    for vm in json_data:
        if vm.get("name") == args.name:
            data = vm.get("vm")
            return data
