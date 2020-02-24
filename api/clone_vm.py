#!/usr/bin/env python3

__author__ = "Mark Chard | machard.1984@gmail.com"

import esxi
import datastore
import library
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
        template_id = library.find(args, authenticated)

    if args.datastore:
        datastore_id = datastore.id(args, authenticated)

    if args.esxi_host:
        host_id = esxi.id(args, authenticated)

    url = "POST https://%s/rest/com/vmware/vcenter/ovf/library-item/id:%s?~action=deploy" %(args.vcenter, template_id)
    headers = {
        'content-type': 'application/json'
        'vmware-api-session-id': authenticated
    }
    header_data = {
        "deployment_spec": {
            "name": "test",
            "ovf_library_item_id": template_id,
        }
    }
    data = json.dumps(header_data)
    resp = payload.post_data(url, data, headers)

    disconnect = auth.delete(args, authenticated)

    if disconnect:
        print(disconnect)


if __name__ == "__main__":
    main()
