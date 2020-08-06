import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Your subject here'
msg['From'] = 'your email address from which you want to send the mail'
msg['To'] = 'reciever email address'
msg.set_content('content of your mail')

#if you want to send a file
files = ['hello.txt']

#file type
for file in files:
	with open(file, 'rb') as f:
		file_data = f.read()
		file_name = f.name

	msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

#sending the mail using you email
#you have to set your email settings to less secure app access on
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail:

	mail.login('your email address here', 'your password for login and sending the mail')

	mail.send_message(msg)
	mail.close()


