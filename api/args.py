#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import argparse
import getpass


def build_arg_parser():
    parser = argparse.ArgumentParser(
                        description='Standard Arguments for talking to vCenter')

    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help='Enable debugging')

    parser.add_argument('-o', '--port',
                        type=int,
                        default=443,
                        action='store',
                        help='VCSA Port')

    parser.add_argument('-p', '--password',
                        required=False,
                        action='store',
                        help='VCSA Password')

    parser.add_argument('-s', '--disable_ssl_verification',
                        required=False,
                        action='store_true',
                        help='Disable SSL cert check')

    parser.add_argument('-u', '--user',
                        required=True,
                        action='store',
                        help='VCSA Username')

    parser.add_argument('-L', '--local-library',
                        required=False,
                        action='store',
                        help='Local Library')

    parser.add_argument('-C', '--content-library',
                        required=False,
                        action='store',
                        help='Content Library')

    parser.add_argument('-D', '--datastore',
                        required=False,
                        action='store',
                        help='ESXi datastore name')

    parser.add_argument('-E', '--esxi-host',
                        required=False,
                        action='store',
                        help='ESXi hostname')

    parser.add_argument('-V', '--vcenter',
                        required=True,
                        action='store',
                        help='VCSA hostname')

    parser.add_argument('-N', '--vm-name',
                        required=False,
                        help='VM Name')

    return parser


def prompt_for_password(args):
    if not args.password:
        args.password = getpass.getpass(
            prompt='Enter password for host %s and user %s: ' % (args.vcenter, args.user)
        )
    return args


def get_args():
    parser = build_arg_parser()
    args = parser.parse_args()
    return prompt_for_password(args)
