#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import json

def parse(resp):
    if resp.text:
        data = json.loads(resp.text)
        print(json.dumps(data, indent=2, sort_keys=True))
        return data