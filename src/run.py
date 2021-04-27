from src.logic.tasks import imap_add_flags, imap_remove_flags
from src.configuration.imap import ImapConfig
from src.libs.client import imap
from src.libs.agruments import args


def read_mails(folder: str):
    flag = imap.SEEN
    for user in ImapConfig.imap_users:
        email = user.get("email")
        password = user.get("password")
        imap_add_flags.delay(email, password, folder, flag)


def unread_mails(folder: str):
    flag = imap.SEEN
    for user in ImapConfig.imap_users:
        email = user.get("email")
        password = user.get("password")
        imap_remove_flags.delay(email, password, folder, flag)


if __name__ == "__main__":
    arg = args.__dict__
    if arg.get("read"):
        read_mails(arg.get("read"))
    elif arg.get("unread"):
        unread_mails(arg.get("unread"))
    else:
        print("use ==> python3 src/run.py -h <== for help")
