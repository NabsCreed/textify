import argparse
from re import sub

from numpy import float64
BANNER="""

"""
def parseArguments():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest = 'command')
    login = subparser.add_parser('login')
    list = subparser.add_parser('list')
    pull = subparser.add_parser('pull')
    push =  subparser.add_parser('push')

    push.add_argument('--type', type = str, required=True)
    push.add_argument('--content', type = str, required = True)
    login.add_argument('--ID', type = float64, required=False)
    args = parser.parse_args()
    parseHandler(args)

def parseHandler(args):
    if args.command == 'login':
        print("Logging in")
    elif args.command == 'push':
        print("Push")
    elif args.command == 'pull':
        print('Pull')
    elif args.command == 'list':
        print('List')
    else:
         print("You've typed the wrong command!")