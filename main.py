import smtplib
import dotenv
import os

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage

dotenv.load_dotenv('.env')

server = smtplib.SMTP('smtp.gmail.com', 25)

server.starttls()

print(os.getenv('EMAIL'), os.getenv('PASSWORD'))

server.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))

mail = MIMEMultipart()

mail['From'] = "Python Hub"
mail['To'] = os.getenv('TO')
mail['Subject'] = 'This is a test message'

mail.attach(MIMEText("This a test mail sent with python by pythonhub.", 'plain'))

image = open('image.jpg', 'rb')
audio = open('sample.mp3', 'rb')

imageAttachment = MIMEImage(image.read())
imageAttachment.add_header('Content-Disposition',
                           'attachment; filename=image.jpg')
mail.attach(imageAttachment)
image.close()

audioAttachment = MIMEAudio(audio.read(), 'mp3')
audioAttachment.add_header('Content-Disposition',
                           'attachment; filename=sample.mp3')
mail.attach(audioAttachment)
audio.close()


message = mail.as_string()

server.sendmail(os.getenv('EMAIL'),
                os.getenv('TO'), message)
