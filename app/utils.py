from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def encrypt(message):
	obj = AES.new('my secret key 23', AES.MODE_CFB, 'This is an IV456')
	endobj = obj.encrypt(message.encode('utf8'))
	encmessage = b64encode(endobj).decode('utf-8')
	return encmessage
def decrypt(message):
	obj = AES.new('my secret key 23', AES.MODE_CFB, 'This is an IV456')
	decobj = obj.decrypt(b64decode(message.encode('utf8')))
	message = decobj.decode("utf-8")
	return message