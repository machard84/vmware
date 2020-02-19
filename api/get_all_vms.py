#!/usr/bin/env python

import requests
from tools import cli
import json

def get_args():
    parser = cli.build_arg_parser()
    my_args = parser.parse_args()
    return cli.prompt_for_password(my_args)


def main():
    args = get_args()

    sess = requests.post("https://vcsa.chardma.org.uk/rest/com/vmware/cis/session",
                         auth=(args.user, args.password),
                         verify=False)

    session_id = sess.json()['value']

    resp = requests.get("https://vcsa.chardma.org.uk/rest/vcenter/vm",
                        verify=False,
                        headers={
                            "vmware-api-session-id": session_id}
                        )
    parsed = json.loads(resp.text)
    print(json.dumps(parsed, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()