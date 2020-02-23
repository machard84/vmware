#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import args
import auth
import library
import urllib3


def get_args():
    parser = args.build_arg_parser()
    parser.add_argument('template',
                        choices=[
                            'list',
                            'info',
                        ])
    my_args = parser.parse_args()
    return args.prompt_for_password(my_args)


def main():
    args = get_args()

    if args.disable_ssl_verification:
        urllib3.disable_warnings()

    authenticated = auth.get(args)

    if args.template == 'list':
        content_library = library.list(args, authenticated)
        print(content_library)

    if args.template == 'info':
        template = library.info(args, authenticated)
        print(template)

    disconnect = auth.delete(args, authenticated)

    if disconnect:
        print(disconnect)


if __name__ == "__main__":
    main()
