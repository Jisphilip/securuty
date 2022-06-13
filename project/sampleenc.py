from cryptography.fernet import Fernet
from werkzeug.utils import secure_filename
import uuid


def enc(message):
	# message = "hello geeks"
	key = Fernet.generate_key()
	print(key)
	fernet = Fernet(key)
	

	encMessage = fernet.encrypt(message)
	encMessage=str(encMessage).replace("b'","")
	encMessage=encMessage.replace("'","")
	details=secure_filename(str(uuid.uuid4()) + ".txt")
	filename =  "static/encmsg/" + details
	file_object = open(filename, 'a')
	# Append 'hello' at the end of file
	file_object.write(encMessage)
	# Close the file
	file_object.close()
	key=str(key).replace("b'","")
	key=key.replace("'","")
	filenames =  "static/keys/" + details
	encMessage
	file_objects = open(filenames, 'a')
	# Append 'hello' at the end of file
	file_objects.write(key)
	# Close the file
	file_objects.close()
	return filename,filenames
	  
def dec(data,key):


	f = open(key, "r")
	# print("ss",f.read())
	# key=key.replace("b","")
	# key=key.replace("'","")
	
	# key=key.
	keys=f.read()
	keyss=keys.encode('utf-8')

	print("vf",keyss)

	fernet = Fernet(keyss)
	# print(data)
	f1 = open(data, "r")
	datas=f1.read()
	datass1=datas.encode('utf-8')
	print(datass1)
	
	decMessage = fernet.decrypt(datass1).decode()
	  
	print("decrypted string: ", decMessage)
	return decMessage

# val,key=enc("Haiii")
# dec(val,key)