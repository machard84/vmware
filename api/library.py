#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import payload
import response
import json

def create_library():
    url = "https://%s/rest/vcenter/vm-template/library-items" % (args.vcenter)
    create_library = payload.post(authenticated, url)
    data = response.parse(create_library)
    return data


def local_id(args, authenticated):
    url = "https://%s/rest/com/vmware/content/local-library" % (args.vcenter)
    library_list = payload.get(authenticated, url)
    data = response.parse(library_list)
    url = "https://%s/rest/com/vmware/content/library/id:%s" % (args.vcenter, data)
    data = payload.get(authenticated, url)
    return data


def list(args, authenticated):
    url = 'https://%s/rest/com/vmware/content/library' % args.vcenter
    content = payload.get(authenticated, url)
    data = response.parse(content)
    return data


def info(args, authenticated):
    lib = list(args, authenticated)
    url = "https://%s/rest/com/vmware/content/library/id:%s" % (args.vcenter, lib)
    content = payload.get(authenticated, url)
    data = response.parse(content)
    return data


def create_session(args, authenticated):
    url = "https://%s/rest/com/vmware/content/library/item/download-session" % (args.vcenter)
    content = payload.post(authenticated, url)
    data = response.parse(content)
    return data


def delete_session(args, authenticated):
    url = "https://%s/rest/com/vmware/content/library/item/download-session/id:%s" %(args.vcenter, download_token)
    payload.delete(authenticated, url)


def create_template():
    url = 'https://%s/rest/vcenter/vm-template/library-items' % (args.vcenter)
    content = payload.post(authenticated, url)
    data = response.parse(content)
    return data

def find(args, authenticated):
    url = "https://%s/rest/com/vmware/content/library/item?~action=find" % ( args.vcenter )
    name = (args.vm_name)
    headers = {
        'content-type': 'application/json',
        'vmware-api-session-id': authenticated
    }
    header_data = {
        "spec": {
            "name": name,
        }
    }
    data = json.dumps(header_data)
    resp = payload.post_data(url, data, headers)
    return resp
