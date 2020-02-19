#!/usr/bin/env python
import atexit
from pyVim.connect import SmartConnectNoSSL, SmartConnect, Disconnect
from tools import cli
from pyVmomi import vim

def get_args():
    parser = cli.build_arg_parser()
    parser.add_argument('-j', '--uuid',
                        help='UUID of the VirtualMachine to power on')
    parser.add_argument('-n', '--name',
                        help='DNS Name of the VirtualMachine to power on')
    parser.add_argument('-i', '--ip',
                        help='IP Addres sof the Virtual machine to power on')
    parser.add_argument('command',
                        choices=['poweron', 'poweroff', 'template'])
    my_args = parser.parse_args()
    return cli.prompt_for_password(my_args)


def main():
    args = get_args()
    vm = None
    try:
        if args.disable_ssl_verification:
            si = SmartConnectNoSSL(
                host=args.host,
                user=args.user,
                pwd=args.password,
                port=int(args.port))
            atexit.register(Disconnect, si)
        else:
            si = SmartConnect(
                host=args.host,
                user=args.user,
                pwd=args.password,
                port=int(args.port))
            atexit.register(Disconnect, si)
    except vim.fault.InvalidLogin:
        raise SystemExit("Unable to connect to host"
                         "with supplied credentials")

    if args.uuid:
        vm = si.content.searchIndex.FindByUuid(None, args.uuid, True, True)
    elif args.name:
        vm = si.content.searchIndex.FindByDnsName(None, args.name, True)
    elif args.ip:
        vm = si.content.searchIndex.FindByIp(None, args.ip, True)

    str = "%s %s" % (args.command, args.name)
    print(str)
    if vm:
        if args.command == 'poweron':
            vm.PowerOn()
        elif args.command == 'poweroff':
            vm.ShutdownGuest()
        elif args.command == 'template':
            vm.MarkAsTemplate()
    else:
        raise SystemExit("Unable to locate VM")


if __name__ == "__main__":
   main()
