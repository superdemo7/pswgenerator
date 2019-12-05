import zipfile
import smtplib
import menu
from email.mime.application import MIMEApplication

def send(timer):
    zip_pass = '12345'
    with zipfile.ZipFile('pass.zip', 'w') as myzip:
        myzip.write('config.json')
    gmail_sender = 'ajmv25798@gmail.com'
    gmail_passwd = 'goyxaevyofyircec'

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender,gmail_passwd)
    subject = ''
    body = '\r\n'.join(['To: %s' % to,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % subject,
                        ''])
    msg.attach(MIMEText(text))
    try:
        server.sendmail(gmail_sender,[to],body)
        print('Correo enviado')
        #goyxaevyofyircec
    except:
        print('Error enviando correo')
    server.quit()
    menu.menu(timer)