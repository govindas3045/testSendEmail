import requests
import csv
from datetime import date
import smtplib
from email.message import EmailMessage

'''Downloading the CSV and getting tickers whose reportDate = Todays Date'''
today = str(date.today())
tickers_to_send = []

CSV_URL = f'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=demo'
with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        if row[2] == today:
            tickers_to_send.append(row[0])
            print(row)

'''Sending the email'''
# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'govindsomadas@gmail.com'
sender_password = 'pypj sgmh echi bous'

# List of recipients
recipients = ['govindplaystation4028@gmail.com', 'psdj1997@gmail.com']

# Create the email
msg = EmailMessage()
msg['Subject'] = 'Tickers to Check'
msg['From'] = sender_email
msg['To'] = ', '.join(recipients)
msg.set_content(f'{tickers_to_send}')

try:
    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print('Email sent successfully to multiple recipients!')
except Exception as e:
    print(f'Failed to send email: {e}')
