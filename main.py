from smtplib import (
    SMTP,
    SMTPConnectError,
    SMTPAuthenticationError,
    SMTPException,
    SMTPResponseException,
    SMTPDataError,
)
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage

from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_MAIL = os.getenv("RECEIVER_MAIL")


def connect_to_server() -> SMTP:
    try:
        server = SMTP("smtp.gmail.com", 25)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        return server
    except (SMTPConnectError, SMTPAuthenticationError) as auth_error:
        print(f"Exception Occurred: {auth_error}")
        raise auth_error


def send_multipart_mail():
    mail = MIMEMultipart()

    mail["From"] = "Devzone"
    mail["To"] = RECEIVER_MAIL
    mail["Subject"] = "An automated mail"

    mail.attach(
        MIMEText("This is an image and audio attachment from Devzone", "plain"),
    )

    with open("assets/image.jpg", "rb") as image:
        image_attachment = MIMEImage(image.read())
        image_attachment.add_header(
            "Content-Disposition", "attachment; filename=image.jpg"
        )
        mail.attach(image_attachment)

    with open("assets/sample.mp3", "rb") as audio:
        audio_attachment = MIMEAudio(audio.read(), "mp3")
        audio_attachment.add_header(
            "Content-Disposition", "attachment; filename=sample.mp3"
        )
        mail.attach(audio_attachment)

    message = mail.as_string()

    try:
        server = connect_to_server()
        server.sendmail(os.getenv("EMAIL"), os.getenv("TO"), message)
    except (SMTPException, SMTPResponseException, SMTPDataError) as smtp_error:
        print(f"Exception Occurred: {smtp_error}")


if __name__ == "__main__":
    send_multipart_mail()
