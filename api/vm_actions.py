#!/usr/bin/env python

import requests
from tools import cli
import json


def get_args():
    parser = cli.build_arg_parser()
    parser.add_argument('-n', '--name',
                        help='DNS Name of the VirtualMachine to power on')
    parser.add_argument('power',
                        choices=[
                            'reset',
                            'start',
                            'stop',
                            'suspend',
                            'reboot',
                            'shutdown',
                            'standby',
                        ])
    my_args = parser.parse_args()
    return cli.prompt_for_password(my_args)


def auth():
    sess_url = "https://%s/rest/com/vmware/cis/session" % args.host
    sess = requests.post(sess_url,
                         auth=(args.user, args.password),
                         verify=False)
    session_id = sess.json()['value']
    print(session_id)
    return session_id


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


def inventory():
    url = "https://%s/rest/vcenter/vm" % args.host
    vms = get(authenticated, url)
    json_data = vms["value"]
    for vm in json_data:
        if vm.get("name") == args.name:
            vmid = vm.get("vm")
            return vmid


def main():
    vm_id = inventory()
    if args.power == 'standby' or args.power == 'reboot' or args.power == 'shutdown':
        url = "https://%s/rest/vcenter/vm/%s/guest/power?action=%s" % (args.host, vm_id, args.power)
        post(authenticated, url)

    if args.power == 'start' or args.power == 'stop' or args.power == 'reset' or args.power == 'suspend':
        url = "https://%s/rest/vcenter/vm/%s/power/%s" % (args.host, vm_id, args.power)
        post(authenticated, url)

    print(url, authenticated)


if __name__ == "__main__":
    args = get_args()
    authenticated = auth()
    main()
