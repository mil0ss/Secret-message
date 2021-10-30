alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,:;!?()-_ '
print('***Message decryptor***')

message = input('What message do you want to decrypt?:  ')

key = len(message)

key = int(key)

newMessage = ''

for character in message:
	if character in alphabet:
		position = alphabet.find(character)
		newPosition = (position - key) % 73
		newCharacter = alphabet[newPosition]
		newMessage += newCharacter
	else:
		newMessage += character

print('The resut of your decrypted message is: ', newMessage)
print("***Program finished***")