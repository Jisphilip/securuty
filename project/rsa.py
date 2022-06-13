# Inspired from http://coding4streetcred.com/blog/post/Asymmetric-Encryption-Revisited-(in-PyCrypto)
# PyCrypto docs available at https://www.dlitz.net/software/pycrypto/api/2.6/
import random

# import MySQLdb
import pyqrcode
from Crypto import Random
import string

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64
import hashlib




def generate_keys():
		# RSA modulus length must be a multiple of 256 and >= 1024
		modulus_length = 256*4 # use larger value in production
		randomnum=''.join(random.choice(string.hexdigits) for n in range(modulus_length))
		publickey = RSA.generate(modulus_length, Random.new().read)
		privatekey  = publickey.publickey()
		return privatekey, publickey

def encrypt_message(a_message , privatekey):
		# print(publickey.encrypt("Hello.".encode('utf-8'), 32))
		encryptor = PKCS1_OAEP.new(privatekey)
		encrypted = encryptor.encrypt(a_message.encode('utf-8'))
		# encrypted_msg = privatekey.encrypt(a_message.encode('utf-8'), 32)[0]
		encoded_encrypted_msg = base64.b64encode(encrypted) # base64 encoded strings are database friendly
		return encoded_encrypted_msg



def decrypt_message(encoded_encrypted_msg, publickey):
		decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)


		# print('okkkk')
		# print(decoded_encrypted_msg)
		# print('end')
		encryptor = PKCS1_OAEP.new(publickey)
		decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
		return decoded_decrypted_msg

########## BEGIN ##########

# a_message = "The quick brown fox jumped over the lazy dog"
# privatekey , publickey = generate_keys()
# encrypted_msg = encrypt_message(a_message , privatekey )
# decrypted_msg = decrypt_message(encrypted_msg, publickey)
#
# print ("%s - (%d)" % (privatekey.exportKey() , len(privatekey.exportKey())))
# print ("%s - (%d)" % (publickey.exportKey() , len(publickey.exportKey())))
# print (" Original content: %s - (%d)" % (a_message, len(a_message)))
# print ("Encrypted message: %s - (%d)" % (encrypted_msg, len(encrypted_msg)))
# print ("Decrypted message: %s - (%d)" % (decrypted_msg, len(decrypted_msg)))


privatekey, publickey = generate_keys()
# print("pub" + str(privatekey.exportKey()))
encrypted_msg = encrypt_message("hello", privatekey)
# print("ec", str(encrypted_msg))
# con=MySQLdb.connect(host='localhost',port=3308,user='root',passwd='root',db='uniqueid')
# cmd=con.cursor()
# print(publickey)
# print(type(publickey))
ky=publickey.exportKey("PEM")
pky=privatekey.exportKey("PEM")



# key = publickey[0]

# pk = RSA.importKey(key)
# print('pk--------------', pk)
decrypted_msg = decrypt_message(encrypted_msg, publickey)
# print("decy msg" , decrypted_msg)

with open ("private.pem", "w") as prv_file:
	print("{}".format(publickey.exportKey()), file=prv_file)
