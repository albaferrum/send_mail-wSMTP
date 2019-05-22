import smtplib
gonderici_mail = "cemakdemir99@gmail.com"
gonderici_sifre = "sifreniz"
alicilar = ["alici@gmail.com"]
mesaj = """From: Cem Akdemir <cemakdemir99@gmail.com>
To: Cahit Silleli <cahitsilleli@gmail.com>
Subject: HAREKET ALGILANDI! ALARM VERİLDİ!"""

server = smtplib.SMTP("smtp.gmail.com" , 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(gonderici_mail, gonderici_sifre)

try:
    server.sendmail(gonderici_mail, alicilar, mesaj)
    print "Mail Gönderildi!"
except:
    print "Mail Gönderilemedi!"
server.quit()
