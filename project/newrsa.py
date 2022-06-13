from rsa import *
from werkzeug.utils import secure_filename
import  uuid
from sampleenc import *
from database import *

def encrypt(image):
	privatekey, publickey = generate_keys()
	# print("pub------"+str(publickey))
	# print("prvt---------" + str(privatekey))
	encrypted_msg = encrypt_message(image, privatekey)
	# print(str(encrypted_msg))
	rsa_pvtkey=privatekey.exportKey("PEM")
	# print('rsakeyy---------',rsa_pvtkey)
	rsa_pubkey=publickey.exportKey("PEM")
	print(type(rsa_pubkey))

	details=secure_filename(str(uuid.uuid4()) + ".jpg")
	filename =  "static/uploads/" + details
	print(filename)
	fh = open(filename, "wb")
	fh.write(base64.b64decode(encrypted_msg))
	fh.close()
	val,keys=enc(rsa_pubkey)
	# print(encrypted_msg)
	# print(rsa_pubkey)
	return filename,val,keys
# print('rsapubkeyy---------', rsa_pubkey)
# rsa_pub = PKCS1_OAEP.new(rsa_pubkey)
# print("mnb",str(encrypted_msg.decode('utf-8'))+" ppppppprrr "+rsa_pvtkey.decode('utf-8')+"  puuuuuuu "+rsa_pubkey.decode('utf-8'))



def decrypt(mid):
# //////////////
	print("decrypt")
	q="select * from files where file_id='%s'" %(mid)
	res=select(q)
	with open(res[0]['file'], "rb") as imageFile:
		data = base64.b64encode(imageFile.read()).decode('utf-8')
	print(data.encode('utf-8'))
	encrypted_msg=data
	val=res[0]['encval']
	keys=res[0]['key']
	rsa_pubkey=dec(val,keys)
	print(rsa_pubkey)
	# key=publickey[0]
	pk = RSA.importKey(rsa_pubkey.encode('utf-8'))
	
	# print('pk--------------',pk)
	decrypted_msg =decrypt_message(encrypted_msg,pk)
	print("decy msg"+ str(decrypted_msg))
	print(decrypted_msg)
	data = str(decrypted_msg.decode('utf-8')).split('#')
	ipd=data[0]


	print(ipd)
	return ipd

	

	
