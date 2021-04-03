import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import date

def send(filename):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ptn8403@gmail.com', '**********')

    #today = str(date.today())+".csv"

    from_address = 'ptn8403@gmail.com'
    to_address = 'bora.yuret@bilgeadam.com'



    subject = "Yfscraper'dan mail geldi! " + filename

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    body = """<b>Selamlar</b> <hr/> 
              Python programından mail gönderiyoruz. <br/> 
              bora öçşiğüı <hr/>
              <a href="https://www.iskultur.com.tr/">İş Bankası Kültür Yayınları</a>"""

    msg.attach(MIMEText(body, 'html'))


    my_attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    #part = MIMEBase('application', 'pdf')
    part.set_payload(my_attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename='+filename)
    msg.attach(part)


    message = msg.as_string()


    #for to_single in to_list:
    server.sendmail(from_address, to_address, message)

    server.quit()