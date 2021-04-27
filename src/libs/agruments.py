import argparse

parser = argparse.ArgumentParser()
arg = parser.add_mutually_exclusive_group()
arg.add_argument(
    "-r",
    "--read",
    type=str,
    help="read mails in a folder",
)

arg.add_argument(
    "-u",
    "--unread",
    type=str,
    help="unread mails in a folder",
)
args = parser.parse_args()
