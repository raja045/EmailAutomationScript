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
  - **SMTP** access enabled.
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
4. **Replace the file path to your CSV file**:
   ```python
   file_path = '/path/to/emaillist.csv'
5. Customize the email subject and body as needed in the script.

---

## Usage (If you have a python environment ready)
1. Run the script in your Python environment:
   ```bash
   python3 email_automation.py
2. The script will loop through the recipient list and send the email to each address.
3. Monitor the console for status updates on email delivery.
   
## Usage 2.0 ( If you do not have a python Environment)
1. Creating an python environment in easiest way.
   - Visit the site and create an account, https://colab.google
   - Click on File > Open a New NoteBook
     
2. Open the .ipynb file provided above.
3. make the necessary changes and run the above file.

---

### Useful Resources:
- [How to find the APP password for the google account](https://www.hostpapa.com/knowledgebase/how-to-create-and-use-google-app-passwords/)
- [How to convert the Normal email text into HTML content](https://www.textfixer.com/html/convert-email-to-html.php)

