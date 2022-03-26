from email.mime.text import MIMEText
import smtplib
import dns.resolver
def send_mail(email,height,average_height,count):
    from_id="omkar18rajmane@gmail.com"
    from_pwd="wgeskahakiaxruof"
    to__=email

    sub="Participation in Height Survey"
    message="Hey There Ur height is <strong>%s<strong>.The Average Height So far is %s,this out of a pool of %s people"%(height,average_height,count)
    msg=MIMEText(message,'html')
    msg["To"]=to__
    msg["Subject"]=sub
    msg["From"]=from_id

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_id,from_pwd)
    gmail.send_message(msg)

def verify_email(email):
    records = dns.resolver.query(email, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)
    print(mxRecord)

#


