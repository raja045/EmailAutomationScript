# -*- coding: utf-8 -*-
"""HTMLFormat - EmailAutomationScript.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1itQ81XpofC-LUfjE26obYY8GZ1m0iaJE
"""

!pip install pandas

import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load email list from a CSV or Excel file
file_path = 'path_to_the_CSV_File_in_the_Colab_NoteBook'  # replace with your file path
df = pd.read_csv(file_path)  # Use pd.read_excel('emails.xlsx') for Excel files

# Email setup
sender_email = "sender's email address"
sender_password = "This is App Password, Not the actual password of your google account."  # For Gmail, consider an App Password if 2FA is enabled

# SMTP server configuration (for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Secure the connection
server.login(sender_email, sender_password)

# Loop through each recipient in the file and send the email
for index, row in df.iterrows():
    recipient_email = row['Email']
    recipient_name = row['Name']  # Optional, for personalized messages

    # Create the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = "Subject of the email"

    # Email body (personalize if needed)
    body = f"""
    <html>
    <body>
    <p>Dear {recipient_name},</p>
    <p> Change me </p>
    </body>
    </html>
    """

    # Attach the HTML body to the email
    message.attach(MIMEText(body, 'html'))

    # Send the email
    try:
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

# Close the SMTP server connection
server.quit()