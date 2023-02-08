# Python Mailer Script

This script demonstrates the use of the SMTP package in Python to send emails.

## Requirements
- smtplib
- email libraries

## Usage
1. Import the necessary libraries and set up the SMTP connection with your mail server.
2. Compose your email message and specify the recipient(s) and sender information.
3. Use the `sendmail` method to send the email.

## Example
This script provides a basic example of sending an email with a subject, recipient, sender, and message body. You may need to adjust the code to fit your specific use case, such as adding attachments or configuring security settings.

## Poetry Setup
You can also use [Poetry](https://python-poetry.org/) as your package manager.

1. Install Poetry with `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python` or `pip3 install poetry`.
2. Install the packages with `poetry install`.
3. Spawn a new shell with `poetry shell`

## Note
Before running the script, make sure to check your email provider's policies on sending automated emails. Some providers may restrict or block such activity, so it's important to verify this in advance.
