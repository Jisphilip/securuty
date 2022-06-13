from flask import *
from database import *
import demjson
import uuid
from newrsa import *
import uuid
import qrcode
import random
from werkzeug.utils import secure_filename
import cv2
from madosemail import *

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail




api=Blueprint("api",__name__)


@api.route('/login',methods=['get','post'])
def login():
	data={}
	
	username = request.args['username']
	password = request.args['password']
	q="SELECT * from login inner join employee using(login_id) where username='%s' and password='%s'" % (username,password)
	print(q)
	res = select(q)
	print(res)
	if res :
		data['status']  = 'success'
		data['data'] = res
		
	else:
		data['status']	= 'failed'
	data['method']='login'
	return  demjson.encode(data)



@api.route('/employeeviewprofile')
def employeeviewprofile():
	data={}
	lid=request.args['lid']
	q="select * from employee where employee_id=(select employee_id from employee where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="employeeviewprofile"
	return demjson.encode(data)


@api.route('/employeeeditprofile')
def employeeeditprofile():
	data={}
	lid=request.args['lid']
	fname=request.args['fname']
	lname=request.args['lname']
	place=request.args['place']
	phone=request.args['phone']
	email=request.args['email']
	qualification=request.args['qualification']
	q="update employee set first_name='%s',last_name='%s',place='%s',phone='%s',email='%s',qualification='%s' where login_id='%s'"%(fname,lname,place,phone,email,qualification,lid)
	update(q)
	data['status']="success"
	data['method']="employeeeditprofile"
	return demjson.encode(data)

@api.route('/employeeaddfeedback')
def employeeaddfeedback():
	data={}
	feedback=request.args['feedback']
	lid=request.args['lid']
	q="insert into feedback values(null,(select employee_id from employee where login_id='%s'),'%s',curdate())"%(lid,feedback)
	insert(q)
	data['status']="success"
	data['method']="employeeaddfeedback"
	return demjson.encode(data)

@api.route('/employeeviewfeedback')
def employeeviewfeedback():
	data={}
	lid=request.args['lid']
	q="select * from feedback where employee_id=(select employee_id from employee where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="employeeviewfeedback"
	return demjson.encode(data)

@api.route('/Employee_upload_files',methods=['get','post'])
def Employee_upload_files():

	data={}
	number = random.randint(1000,9999)
	path = ""
	title=request.form['title']
	file_types=request.form['file_types']
	logid=request.form['logid']
	q="select email from employee where login_id='%s'" %(logid)
	res=select(q)
	email=res[0]['email']
	image=request.files['image']
	# ftype = request.form['ftype']
 
	path='static/uploads/'+str(uuid.uuid4())+image.filename
	image.save(path)

	if file_types=="Type1":
		q="INSERT INTO `files` VALUES(NULL,(SELECT `employee_id` FROM `employee` WHERE `login_id`='%s'),'%s','%s',CURDATE(),'%s','','','')"%(logid,title,file_types,path)
		print(q)
		id=insert(q)
	elif file_types=="Type2":
		# file,keys=encrypt(path)
		file,val,keys=encrypt(path)
		
		# decrypted_msg = decrypt_message(encrypted_msg, publickey)
		q="INSERT INTO `files` VALUES(NULL,(SELECT `employee_id` FROM `employee` WHERE `login_id`='%s'),'%s','%s',CURDATE(),'%s','%s','%s','%s')"%(logid,title,file_types,file,keys,val,number)
		id=insert(q)
		try:
			gmail = smtplib.SMTP('smtp.gmail.com', 587)
			gmail.ehlo()
			gmail.starttls()
			gmail.login('projectsriss2020@gmail.com','messageforall')
		except Exception as e:
			print("Couldn't setup email!!"+str(e))
		msg='Your Key for the title '+title+' is '+str(number)
		msg = MIMEText(msg)

		msg['Subject'] = "Key"

		msg['To'] = email

		msg['From'] = 'projectsriss2020@gmail.com'

		try:

			gmail.send_message(msg)
			print(msg)


		except Exception as e:
			print("COULDN'T SEND EMAIL", str(e))

	elif file_types=="Type3":
		file,val,keys=encrypt(path)
		
		# decrypted_msg = decrypt_message(encrypted_msg, publickey)
		q="INSERT INTO `files` VALUES(NULL,(SELECT `employee_id` FROM `employee` WHERE `login_id`='%s'),'%s','%s',CURDATE(),'%s','%s','%s','%s')"%(logid,title,file_types,file,keys,val,number)
		id=insert(q)
		path = "static/qrcode/" + title + ".png"
		img = qrcode.make(str(id))
		img.save(path)
		filesssss(path,email,title,number)	
	elif file_types=="Type4":
		file,val,keys=encrypt(path)
		
		# decrypted_msg = decrypt_message(encrypted_msg, publickey)
		q="INSERT INTO `files` VALUES(NULL,(SELECT `employee_id` FROM `employee` WHERE `login_id`='%s'),'%s','%s',CURDATE(),'%s','%s','%s','%s')"%(logid,title,file_types,file,keys,val,number)
		id=insert(q)
		path = "static/qrcode/" + title + ".png"
		img = qrcode.make(str(id))
		img.save(path)

		filesssss(path,email,title,number)		
		

	data['status'] = 'success'
	data['method'] = 'Employee_upload_files'
	return demjson.encode(data)



@api.route('/Employee_view_uploaded_files')
def Employee_view_uploaded_files():
	data={}
	login_id=request.args['login_id']
	q="SELECT * FROM `files` WHERE `employee_id`= (SELECT `employee_id` FROM `employee` WHERE `login_id`='%s')"%(login_id)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="Employee_view_uploaded_files"
	return demjson.encode(data)

@api.route('/verifyfiles')
def verifyfiles():
	data={}
	fid=request.args['fid']
	content=request.args['content']
	q="select * from files where file_id='%s' and basekey='%s' "%(fid,content)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="verifyfiles"
	return demjson.encode(data)


@api.route('/downloadfile',methods=['get','post'])
def downloadfile():

    datas = {}

    mid = request.args['mid']
    path=decrypt(mid)
    # # data = download(mid)
    print("path : "+path)

    # filename="static/downloads/"+str(uuid.uuid4())+path[:-1]
   
    # file = open(path, "rb")
    # data = file.read()
    # # pritn(data)


    datas['status']='success'
    datas['path']=path
    datas['method']='downloadfile'
    
    return demjson.encode(datas)


@api.route('/checkqr',methods=['get','post'])
def checkqr():

    datas = {}

    image = request.files['image']
    path="static/checkqr/"+str(uuid.uuid4())+".png"
    image.save(path)
    # Name of the QR Code Image file
	# read the QRCODE image
    image = cv2.imread(path)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    # detect and decode
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    # if there is a QR code
    # print the data
    if vertices_array is not None:
    	print(data)
    else:
        print("There was some error") 

    datas['status']='success'
    datas['out']=data
    datas['method']='checkqr'
    
    return demjson.encode(datas)