#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import payload


def id(args, authenticated):
    url = "https://%s/rest/vcenter/datastore" % (args.vcenter)
    list = payload.get(authenticated, url)
    json_data = list["value"]
    for datastore in json_data:
        if datastore.get("name") == args.datastore:
            data = datastore.get("datastore")
            return data
