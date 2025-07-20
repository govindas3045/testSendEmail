import smtplib
from email.message import EmailMessage

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'govindsomadas@gmail.com'
sender_password = 'pypj sgmh echi bous'

# List of recipients
recipients = ['govindplaystation4028@gmail.com', 'psdj1997@gmail.com']

# Create the email
msg = EmailMessage()
msg['Subject'] = 'Test Email'
msg['From'] = sender_email
msg['To'] = ', '.join(recipients)  # Display in "To" header
msg.set_content('Open it. https://www.youtube.com/watch?v=sVMW45oGP7s')

try:
    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print('Email sent successfully to multiple recipients!')
except Exception as e:
    print(f'Failed to send email: {e}')