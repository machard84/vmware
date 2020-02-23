#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import payload


def id(args, authenticated):
    url = "https://%s/rest/vcenter/host" % (args.vcenter)
    list = payload.get(authenticated, url)
    json_data = list["value"]
    for esxi in json_data:
        if esxi.get("name") == args.esxi_host:
            data = esxi.get("host")
            return data
