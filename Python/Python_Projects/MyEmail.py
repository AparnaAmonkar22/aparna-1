import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email Info
sender_emailId = input('Please enter sender email: ') #'aparn.amonkar@gmail.com'
sender_password = input('Please enter sender password: ')
subject = 'Sample Email'
body = 'This is a sample email'
receiver_emailIds = ['bablo.amonkar@gmail.com', 'visitaparnanaik@gmail.com']

# Configuration
smtp_server = 'smtp.gmail.com'
port = 587

# Create a message
message = MIMEMultipart()
#message = MIMEText(body, 'plain')
message['From'] = sender_emailId
# Join the list of receiver emails into a string separated by commas
message["To"] = ", ".join(receiver_emailIds)
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Send the email
# Create smtp server
server = smtplib.SMTP(smtp_server, port)
server.ehlo()
# Secure the connection
server.starttls()
server.ehlo()
print("Server Connected")


server.login(sender_emailId, sender_password)
print('Logged In')
server.sendmail(sender_emailId, receiver_emailIds, message.as_string())
print('Email Sent!')

# Close the connection
server.quit()

