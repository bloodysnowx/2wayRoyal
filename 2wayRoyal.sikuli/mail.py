import smtplib
from email.mime.text import MIMEText

class Mailer:
    def __init__(self, from, pass, to)
    username = from
    password = pass
    target = to
    host = 'smtp.gmail.com'
    port = 587
    
    def execute(self, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = self.to

        smtp = smtplib.SMTP(self.host, self.port)
        smtp.set_debuglevel(1)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.username, self.password)
        smtp.sendmail(self.username, self.target, msg.as_string())
        smtp.quit()
