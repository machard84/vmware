#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import payload


def create_library():
    url = "https://%s/rest/vcenter/vm-template/library-items" % (args.vcenter)
    create_library = payload.post(authenticated, url)
    data = common(create_library)
    return data


def local_id(args, authenticated):
    url = "https://%s/rest/com/vmware/content/local-library" % (args.vcenter)
    library_list = payload.get(authenticated, url)
    lib_list = common(library_list)
    url = "https://%s/rest/com/vmware/content/library/id:%s" % (args.vcenter, lib_list)
    data = payload.get(authenticated, url)
    return data


def list(args, authenticated):
    url = 'https://%s/rest/com/vmware/content/library' % args.vcenter
    content = payload.get(authenticated, url)
    data = common(content)
    return data


def info(args, authenticated):
    lib = list(args, authenticated)
    url = "https://%s/rest/com/vmware/content/library/id:%s" % (args.vcenter, lib)
    content = payload.get(authenticated, url)
    data = common(content)
    return data


def create_session(args, authenticated):
    url = "https://%s/rest/com/vmware/content/library/item/download-session" % (args.vcenter)
    content = payload.post(authenticated, url)
    data = common(content)
    return data


def delete_session(args, authenticated):
    url = "https://%s/rest/com/vmware/content/library/item/download-session/id:%s" %(args.vcenter, download_token)
    payload.delete(authenticated, url)


def create_template():
    url = 'https://%s/rest/vcenter/vm-template/library-items' % (args.vcenter)
    content = payload.post(authenticated, url)
    data = common(content)
    return data

def common(content):
    json_data = content["value"]
    for data in json_data:
        return data