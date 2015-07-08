import smtplib
import os.path
from email.mime.text import MIMEText
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart

from javax.imageio import ImageIO;
from java.io import File

class Mailer:
    def __init__(self, sender, passwd, to):
        self.username = sender
        self.password = passwd
        self.target = to
        self.host = 'smtp.gmail.com'
        self.port = 587
    
    def execute(self, subject, body, picture):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = self.target

        related = MIMEMultipart('related')
        alt = MIMEMultipart('alternative')
        related.attach(alt)
        content = MIMEText(body, 'plain')
        alt.attach(content)

        if picture:
            fp = file(picture.filename, 'rb')
            image = MIMEImage(fp.read(), 'png', name='image.png')
            fp.close()
            related.attach(image)

        msg.attach(related)

        smtp = smtplib.SMTP(self.host, self.port)
        #smtp.set_debuglevel(1)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.username, self.password)
        smtp.sendmail(self.username, self.target, msg.as_string())
        smtp.quit()
        
