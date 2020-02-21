#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import requests
import json


def get(args):
    sess_url = "https://%s/rest/com/vmware/cis/session" % args.host
    sess = requests.post(sess_url,
                         auth=(args.user, args.password),
                         verify=False)
    session_id = sess.json()['value']
    return session_id


def delete(args, authenticated):
    sess_url = "https://%s/rest/com/vmware/cis/session" % args.host
    sess = requests.delete(sess_url, verify=False,
                           headers={
                                "vmware-api-session-id": authenticated
                           })
    if sess.text:
        parsed = json.loads(sess.text)
        print(json.dumps(parsed, indent=2, sort_keys=True))
        return parsed
