from src.app.main import app
from src.libs.client.imap import (
    new_imap_client,
    login,
    add_flags,
    remove_flags,
    get_message_ids,
)
from src.configuration.imap import ImapConfig
from src.libs.logger import logger


@app.task
def imap_add_flags(user: str, password: str, folder: str, flag: str):
    with new_imap_client(ImapConfig.host, ImapConfig.port) as client:
        logger.info(f"ADD FLAGS FOR {user}")
        if login(client, user, password):
            logger.info(f"ADD FLAGS FOR {user}")
            message_ids = get_message_ids(client, folder)
            add_flags(client, folder, message_ids, bytes(flag, "utf-8"))
            logger.info(f"ADD FLAG: {flag}")
            return f"ADD FLAG DONE | {user}"


@app.task
def imap_remove_flags(user: str, password: str, folder: str, flag: str):
    with new_imap_client(ImapConfig.host, ImapConfig.port) as client:
        if login(client, user, password):
            logger.info(f"REMOVE FLAGS FOR {user}")
            message_ids = get_message_ids(client, folder)
            remove_flags(client, folder, message_ids, bytes(flag, "utf-8"))
            logger.info(f"REMOVE FLAGS: {flag}")
            return f"REMOVE FLAG DONE | {user}"
