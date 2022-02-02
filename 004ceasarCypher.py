print('Welcome to Ceasar Cypher')
indexAlfabet = [char for char in 'qwertyuioppåasdfghjkløæzxcvbnm qwertyuiopåasdfghjkløæzxcvbbnm ']

def encrypt(plainText,key):
  return ''.join([indexAlfabet[indexAlfabet.index(char.lower())+key] for char in plainText])

def decrypt(encryptedText,key):
  return ''.join([indexAlfabet[indexAlfabet.index(char)-key] for char in encryptedText])

message = input('Please write your message: ')
encryptionKey = int(input('Please write a number for encryption: '))

print(encrypt(message,encryptionKey))
encryptedText = encrypt(message,encryptionKey)
print(decrypt(encryptedText,encryptionKey))

