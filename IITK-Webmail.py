import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body, to_email, cc_email=None, bcc_email=None, attachment_path=None):
    smtp_server = 'mmtp.iitk.ac.in'
    smtp_port = 25

    # Sender's email address 
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    if cc_email:
        message['Cc'] = cc_email
        message['To'] += ', ' + cc_email
    if bcc_email:
        message['Bcc'] = bcc_email
    if attachment_path:
        attach_file(attachment_path, message)
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()

        server.login(sender_email, sender_password)

        server.sendmail(sender_email, [to_email, cc_email, bcc_email], message.as_string())

    print("Email sent successfully.")

def attach_file(file_path, message):
    attachment = open(file_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {file_path}")
    message.attach(part)


subject = "Write Subject"
body = "Write Body"
to_email = "recipient email id"
cc_email =""
bcc_email = ""
attachment_path = ""
# Don't Forgot to change your email id above.
send_email(subject, body, to_email, cc_email, bcc_email, attachment_path)
