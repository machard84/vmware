#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import args
import auth
import vm
import payload
import urllib3


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
                        ])
    my_args = parser.parse_args()
    return args.prompt_for_password(my_args)


def main():
    args = get_args()

    if args.disable_ssl_verification:
        urllib3.disable_warnings()

    authenticated = auth.get(args)
    vm_id = vm.id(args, authenticated)

    if args.power == 'standby' or args.power == 'reboot' or args.power == 'shutdown':
        url = "https://%s/rest/vcenter/vm/%s/guest/power?action=%s" % (args.vcenter, vm_id, args.power)
        payload.post(authenticated, url)

    if args.power == 'start' or args.power == 'stop' or args.power == 'reset' or args.power == 'suspend':
        url = "https://%s/rest/vcenter/vm/%s/power/%s" % (args.vcenter, vm_id, args.power)
        payload.post(authenticated, url)

    disconnect = auth.delete(args, authenticated)

    if disconnect:
        print(disconnect)


if __name__ == "__main__":
    main()
