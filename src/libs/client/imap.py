from imapclient import IMAPClient
from src.libs.logger import logger


SEEN = "\\Seen"


def new_imap_client(host, port=143, ssl=False):
    """Connect to imap server.

    Return imapclient instance or None if any exception occurs

    """
    try:
        client = IMAPClient(host, port=port, ssl=ssl)
        if not ssl:
            client.starttls()
        return client
    except Exception as e:
        logger.error(
            "Failed to connect to imap server: %s:%s, reason: %r",
            host,
            port,
            e,
        )


def login(client, username, password):
    """Login client using username and password

    client is IMAPClient instance

    """
    try:
        client.login(username, password)
        return True
    except Exception as e:
        logger.error("Could not login: %r", e)
        return False


def add_flags(client, folder, message_ids, flags):
    """
    message_ids: list of message imap id
    flags: list of IMAP flags, \Seen \Answered \Flagged \Deleted \Draft \Recent
           or custom keywords
    """
    try:
        client.select_folder(folder)
        client.add_flags(message_ids, flags)
        return True
    except Exception as e:
        logger.error("Could not set flag for message: %r", e)
        return False


def remove_flags(client, folder, message_ids, flags):
    """
    message_ids: list of message imap id
    flags: list of IMAP flags, \Seen \Answered \Flagged \Deleted \Draft \Recent
           or custom keywords
    """
    try:
        client.select_folder(folder)
        client.remove_flags(message_ids, flags)
        return True
    except Exception as e:
        logger.error("Could not set flag for message: %r", e)
        return False


def get_message_ids(client, folder):
    try:
        client.select_folder(folder)
        msg_ids = client.search()
        return msg_ids
    except Exception as e:
        logger.error("Could not get message id: %r", e)
    return []
