#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import requests
import json


def get(authenticated, url):
    resp = requests.get(url,
                        verify=False,
                        headers={
                            "vmware-api-session-id": authenticated
                        })
    parsed = common(resp)
    return parsed


def post(authenticated, url):
    resp = requests.post(url,
                         verify=False,
                         headers={
                             "vmware-api-session-id": authenticated
                         })
    parsed = common(resp)
    return parsed


def delete(authenticated, url):
    resp = requests.delete(url,
                           verify=False,
                           headers={
                               "vmware-api-session-id": authenticated
                           })
    parsed = common(resp)
    return parsed


def common(resp):
    if resp.text:
        data = json.loads(resp.text)
        print(json.dumps(data, indent=2, sort_keys=True))
        return data
