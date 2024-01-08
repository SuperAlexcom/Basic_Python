from imaplib import IMAP4_SSL
import os
from dotenv import load_dotenv
from email.parser import BytesParser, Parser
from email.policy import default
import email
from time import sleep

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
IMAP_HOST = os.getenv('IMAP_HOST')
IMAP_PORT = os.getenv('IMAP_PORT')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')
PERIOD_CHECK = int(os.getenv('PERIOD_CHECK'))


with IMAP4_SSL(IMAP_HOST, IMAP_PORT) as M:
    rc, resp = M.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    while True:
        M.select()
        status, search_data = M.search(None, '(FROM "test.for.miet@gmail.com")', '(UNSEEN)')
        msgs = search_data[0].split()
        print("Found",len(msgs), "messages")
        for num in msgs:
            typ, data = M.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            body = email_message.get_payload()[0].get_payload(decode=True).decode('utf-8')
            subject = int(email_message['Subject'])

            with open("application_numbers.txt", "r") as f:
                application_numbers = [int(line) for line in f]
            if subject in application_numbers:
                log = open("success_request.log", "a")
            else:
                log = open("error_request.log", "a")
            log.write("%s: %s\n" % (subject, body))
            log.close()
        sleep(PERIOD_CHECK)