import smtplib

def send_mail():
	gmail_user:'coronajhapa12@gmail.com'
	password:'corona@123'
	sent_from:'gmail_user'
	to:'beingkiran88@gmail.com'

	try:
		server=smtplib.SMTP_SSL('smptp.gmail.com',465)
		server.ehlo()
		print('connected to server')
		server.login(gmail_user,password)
		print('logged in susccesfully')
		content(sent_from,to)
		server.send_mail(sent_from,to,content)
		print('email sent succesufully')

	except:
		print('something went wrong')

def email_content(sent_from,to):
	subject:"super important message"
	body:"hello this is sent email"
	email_text="""/
	From:"%s"
	To:"%S"
	Subject:"%s"
	%s
	"""%(sent_from,",".join(to),Subject,body)
	return emai_text

def send_email():


