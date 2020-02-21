#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import argparse
import getpass


def build_arg_parser():
    parser = argparse.ArgumentParser(
                        description='Standard Arguments for talking to vCenter')

    parser.add_argument('-D', '--debug',
                        action='store_true',
                        help='Enable debugging')

    parser.add_argument('-o', '--port',
                        type=int,
                        default=443,
                        action='store',
                        help='VCSA Port')

    parser.add_argument('-n', '--name',
                        help='VM Name')

    parser.add_argument('-p', '--password',
                        required=False,
                        action='store',
                        help='VCSA Password')

    parser.add_argument('-s', '--host',
                        required=True,
                        action='store',
                        help='VCSA Host')

    parser.add_argument('-S', '--disable_ssl_verification',
                        required=False,
                        action='store_true',
                        help='Disable ssl host certificate verification')

    parser.add_argument('-u', '--user',
                        required=True,
                        action='store',
                        help='VCSA User')
    return parser


def prompt_for_password(args):
    if not args.password:
        args.password = getpass.getpass(
            prompt='Enter password for host %s and user %s: ' % (args.host, args.user)
        )
    return args


def get_args():
    parser = build_arg_parser()
    args = parser.parse_args()
    return prompt_for_password(args)
