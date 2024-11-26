# EmailAutomationScript
This Python script automates the process of sending personalized emails to a list of recipients. It is specifically designed for outreach campaigns like inviting participants to volunteer programs or events.


## Features

- **Personalized Emails**: Sends customized emails with recipient-specific details such as name and email.
- **HTML Email Content**: Supports rich HTML content for visually appealing emails.
- **Batch Processing**: Handles bulk email sending efficiently from a CSV or Excel file.
- **SMTP Integration**: Connects seamlessly with the Gmail SMTP server for reliable email delivery.

---

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x** installed on your system.
2. Required libraries: `pandas`, `smtplib`, `email`.  
   Install these libraries using:
   ```bash
   pip install pandas
3. A Gmail account with:
  - **SMTP access enabled**.
  - **App Password** if two-factor authentication (2FA) is active.

## Setup Instructions
1. **Clone this repository** or **download the script file**.
2. **Prepare your recipient list** in a CSV file with the following columns:
   - `Email`: Recipient's email address.
   - `Name`: Recipient's name.
3. **Update the script with your Gmail credentials**:
   ```python
   sender_email = "your-email@gmail.com"
   sender_password = "your-app-password"

