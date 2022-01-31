import smtplib

content = "Mail icergi"

mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()

mail.starttls()

mail.login("Maili gonderecek mail hesabi", "Mail hesabinin sifresi")

mail.sendmail("Maili gonderecek mail hesabi", "Mailin gidecegi hesap",content)