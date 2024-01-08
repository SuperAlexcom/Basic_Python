import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from random import randint


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
IMAP_HOST = os.getenv('IMAP_HOST')
IMAP_PORT = os.getenv('IMAP_PORT')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')
PERIOD_CHECK = os.getenv('PERIOD_CHECK')

HOST = '127.0.0.1'
PORT = 50007

server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
server.starttls()
server.login(EMAIL_LOGIN, EMAIL_PASSWORD)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by ', addr)
        while True:
            email_msg = conn.recv(1024).decode('ascii')
            if not email_msg:
                break
            email, msg = email_msg.split(' ', 1)
            if (not email) or (not msg):
                break
            if '@' not in email:
                conn.sendall(b'Wrong email format')
                continue

            msg_to_sent = MIMEMultipart()
            msg_to_sent['From'] = EMAIL_LOGIN
            msg_to_sent['To'] = email
            application_number = str(randint(0, 10**10))
            msg_to_sent['Subject'] = application_number
            msg_to_sent.attach(MIMEText(msg, 'plain'))
            server.send_message(msg_to_sent)

            msg_to_sent2 = MIMEMultipart()
            msg_to_sent2['From'] = EMAIL_LOGIN
            msg_to_sent2['To'] = EMAIL_LOGIN
            msg_to_sent2['Subject'] = application_number
            msg_to_sent2.attach(MIMEText(msg, 'plain'))
            server.send_message(msg_to_sent2)

            with open("application_numbers.txt", "a") as f:
                f.write(application_number)
            conn.sendall(b'OK')
server.quit()