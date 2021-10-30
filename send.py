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

print('***Message sent***')
