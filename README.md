# Read-Mail
script to mark all read/unread mails, which in a folder for various accounts

# Usage

create your virtualenv: ```python3 -m venv venv```

install package: ```pip install -r requirements.txt```

create ```config.json```


## RABBITMQ
run ```rabbitmq-server.service```

## CELERY
run ```celery -A src.logic.tasks worker -l INFO```

## RUN SCRIPT

```python3 src/run.py -h``` for help

```python3 src/run.py -r INBOX``` read all mails in INBOX folder

```python3 src/run.py -u INBOX``` unread all mails in INBOX folder
