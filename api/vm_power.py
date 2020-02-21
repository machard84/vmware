#!/usr/bin/env python

__author__ = "Mark Chard | machard.1984@gmail.com"

import args
import auth
import inventory
import payload
import urllib3

urllib3.disable_warnings()


def get_args():
    parser = args.build_arg_parser()
    parser.add_argument('power',
                        choices=[
                            'reset',
                            'start',
                            'stop',
                            'suspend',
                            'reboot',
                            'shutdown',
                            'standby',
                        ],
                        )
    my_args = parser.parse_args()
    return args.prompt_for_password(my_args)


def main():
    args = get_args()
    authenticated = auth.get(args)
    vm_id = inventory.get(args, authenticated)

    if args.power == 'standby' or args.power == 'reboot' or args.power == 'shutdown':
        url = "https://%s/rest/vcenter/vm/%s/guest/power?action=%s" % (args.host, vm_id, args.power)
        payload.post(authenticated, url)

    if args.power == 'start' or args.power == 'stop' or args.power == 'reset' or args.power == 'suspend':
        url = "https://%s/rest/vcenter/vm/%s/power/%s" % (args.host, vm_id, args.power)
        payload.post(authenticated, url)

    disconnect = auth.delete(args, authenticated)


if __name__ == "__main__":
    main()
