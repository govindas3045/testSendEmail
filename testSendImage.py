import requests
import csv
from datetime import date
import smtplib
from email.message import EmailMessage
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


'''Sending the email'''
# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'govindplaystation4028@gmail.com'
sender_password = 'nvka suug mepj evpp'

# List of recipients
# recipients = ['govindsomadas@gmail.com', 'psdj1997@gmail.com']
recipients = ['govindsomadas@gmail.com']

# Create the email
msg = EmailMessage()
msg['Subject'] = 'TestEmail_021'
msg['From'] = sender_email
msg['To'] = ', '.join(recipients)
msg.set_content("If you're seeing this then it looks like the email content generation fucked up")

# Load HTML template from a file
with open("email-templates/index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

# Build repeated <img> tags
images_folder_path = "./images/plots"
image_files = [f for f in os.listdir(images_folder_path) if os.path.isfile(os.path.join(images_folder_path, f))]

html_insert = "<div>"
for image_file in image_files:
    html_insert += f'<div class="ticker_graph"><img src="cid:{image_file}"></div>'
    html_insert += '</div>'

# image_files = [f for f in os.listdir(images_folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# images_html = "".join([f'<div><img src="cid:{i}"></div>' for i in image_files])
html_content = html_template.replace("{{images}}", html_insert)
print(html_content)

msg.add_alternative(html_content, subtype='html')

for i, image_file in enumerate(image_files):
    image_path = os.path.join(images_folder_path, image_file)
    with open(image_path, "rb") as f:
        img_data = f.read()
        msg.get_payload()[1].add_related(img_data,
                                        maintype="image",
                                        subtype="png",
                                        cid=f"<{image_file}>")
        
try:
    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print('Email sent successfully to multiple recipients!')
except Exception as e:
    print(f'Failed to send email: {e}')
