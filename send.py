from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from random import randint
import getpass
import math
    
#___________________________________

msg = MIMEMultipart()
 
print("***Send an encrypted message***")
    
msg['From'] = input("Type your email here: ")
password = getpass.getpass("Type your password: ")
#password = input("Contrasenya: ")
msg['To'] = input("Email of the destintary: ")
msg['Subject'] = "Enrypted message"


#___________________________________

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,:;!?()-_ '

newMessage = ''

message = input('Message: ')
key = len(message)

for character in message:
	if character in alphabet:
		position = alphabet.find(character)
		newPosition = (position + key) % 73
		newCharacter = alphabet[newPosition]
		newMessage += newCharacter
	else:
		newMessage += character
        
#__________________________________

#From = msg['From']

newMessage = "Encrypted message: " + newMessage

msg.attach(MIMEText(newMessage, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
server.login(msg['From'], password)
 
server.sendmail(msg['From'], msg['To'], msg.as_string())
    
server.quit()

#___________________________________

'''From = msg['From']
#From = bin(From)
a = password
b = ' '.join(format(ord(x), 'x') for x in a)

#___________________________________

msg = MIMEMultipart()
 
msg['From1'] = "milos.ivancic@escolesminguella.org"
contra = "coronavirus"
msg['To1'] = "milos.ivancic@escolesminguella.org"
msg['Subject'] = "Nou accés al teu servidor"

#From = msg['From']


#____________________________________
missatge = "L\'usuari " + From + " acada d'accedir al teu servidor" + "\n" + "Contrasenya: " + b


#____________________________________
msg.attach(MIMEText(missatge, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()

server.login(msg['From1'], contra)
 
server.sendmail(msg['From1'], msg['To1'], msg.as_string())
 
server.quit()'''

print('***Message sent***')