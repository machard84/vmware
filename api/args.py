#!/usr/bin/env python

import argparse
import getpass


def build_arg_parser():

    parser = argparse.ArgumentParser(
                        description='Standard Arguments for talking to vCenter')

    parser.add_argument('-s', '--host',
                        required=True,
                        action='store',
                        help='vSphere service to connect to')

    parser.add_argument('-o', '--port',
                        type=int,
                        default=443,
                        action='store',
                        help='Port to connect on')

    parser.add_argument('-u', '--user',
                        required=True,
                        action='store',
                        help='User name to use when connecting to host')

    parser.add_argument('-p', '--password',
                        required=False,
                        action='store',
                        help='Password to use when connecting to host')

    parser.add_argument('-S', '--disable_ssl_verification',
                        required=False,
                        action='store_true',
                        help='Disable ssl host certificate verification')

    parser.add_argument('-n', '--name',
                        help='DNS Name of the VirtualMachine to power on')

    parser.add_argument('-l', '--list',
                        action='store_true',
                        help='find a vm')

    parser.add_argument('-D', '--debug',
                        action='store_true',
                        help='enable debugging output')
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
