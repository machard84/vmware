#!/usr/bin/env python

import requests
import json

def get(authenticated, url):
    resp = requests.get(url,
                        verify=False,
                        headers={
                            "vmware-api-session-id": authenticated
                        })
    if resp.text:
        parsed = json.loads(resp.text)
        print(json.dumps(parsed, indent=2, sort_keys=True))
        return parsed


def post(authenticated, url):
    resp = requests.post(url,
                         verify=False,
                         headers={
                             "vmware-api-session-id": authenticated
                         })
    if resp.text:
        parsed = json.loads(resp.text)
        print(json.dumps(parsed, indent=2, sort_keys=True))
        return parsed


def delete(authenticated, url):
    resp = requests.delete(url,
                         verify=False,
                         headers={
                             "vmware-api-session-id": authenticated
                         })
    if resp.text:
        parsed = json.loads(resp.text)
        print(json.dumps(parsed, indent=2, sort_keys=True))
        return parsed
