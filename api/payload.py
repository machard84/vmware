#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import requests
import urllib3
import response

def get(authenticated, url):
    resp = requests.get(url,
                        verify=False,
                        headers={
                            "vmware-api-session-id": authenticated
                        })
    data = response.parse(resp)
    return data

def post_data(url, data, headers):
    if 'headers' and 'data':
        urllib3.disable_warnings()
        resp = requests.post(url,
                             verify=False,
                             headers = headers,
                             data = data)
        data = response.parse(resp)
    return data

def post(authenticated, url):
    if authenticated:
        urllib3.disable_warnings()
        resp = requests.post(url,
                             verify=False,
                             headers={
                                 "vmware-api-session-id": authenticated
                             })
        data = response.parse(resp)
    return data

def delete(authenticated, url):
    resp = requests.delete(url,
                           verify=False,
                           headers={
                               "vmware-api-session-id": authenticated
                           })
    data = response.parse(resp)
    return data
