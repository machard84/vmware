#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import esxi
import datastore
import vm
import auth
import urllib3
import args


def get_args():
    parser = args.build_arg_parser()
    my_args = parser.parse_args()

    if my_args.disable_ssl_verification:
        urllib3.disable_warnings()

    return args.prompt_for_password(my_args)


def main():
    args = get_args()
    authenticated = auth.get(args)


    if args.vm_name:
        vm_id = vm.find(args, authenticated)

    if args.datastore:
        datastore_id = datastore.id(args, authenticated)

    if args.esxi_host:
        host_id = esxi.id(args, authenticated)

    disconnect = auth.delete(args, authenticated)

    if disconnect:
        print(disconnect)


if __name__ == "__main__":
    main()
