#-*- coding:utf8 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
strFrom = ’akrep_alicem09@hotmail.com’
strTo = ‘cemakdemir99@gmail.com’
msgRoot = MIMEMultipart(‘related’)
msgRoot[‘Subject’] = ‘HAREKET ALGILANDI!’
msgRoot[‘From’] = strFrom
msgRoot[‘To’] = strTo
msgRoot.preamble = ‘Hareket algilanmistir!’

msgAlternative = MIMEMultipart(‘alternative’)
msgRoot.attach(msgAlternative)

msgText = MIMEText(‘HAREKET ALGILANDI! LUTFEN KONUMUNUZDA KONTROL SAGLAYINIZ!’)
msgAlternative.attach(msgText)

msgText = MIMEText(‘<b>Some <i>HTML</i> text</b> and an image.<br><img src=”cid:image1″><br>Nifty!’, ‘html’)
msgAlternative.attach(msgText)

fp = open(‘image1.jpg’, ‘rb’)
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header(‘Content-ID’, ‘<image1>’)
msgRoot.attach(msgImage)
smtp = smtplib.SMTP()
smtp.connect(‘smtp.gmail.com’ , 587)
smtp.login(‘cemakdemir99@gmail.com’, ‘alicem09’)
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
