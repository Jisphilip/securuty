from flask import *
from database import *

admin=Blueprint("admin",__name__)

@admin.route("/admin_home",methods=["get","post"])
def admin_home():
	return render_template('admin_home.html')

@admin.route("/admin_manage_employee",methods=["get","post"])
def admin_manage_employee():
	data={}
	q="select * from employee"
	res=select(q)
	print(res)
	data['employee']=res

	if 'submit' in request.form:
		print("hello")
		first_name=request.form['first_name']
		last_name=request.form['last_name']
		phone=request.form['phone']
		place=request.form['place']
		email=request.form['email']
		qualification=request.form['qualification']
		designation=request.form['designation']
		username=request.form['username']
		password=request.form['password']
		q="insert into login values(NULL,'%s','%s','employee')"%(username,password)
		print(q)
		res=insert(q)
		q1="insert into employee values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,first_name,last_name,place,phone,email,qualification,designation)
		res=insert(q1)
		return redirect(url_for('admin.admin_manage_employee'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=='delete':
		q="delete employee,login from employee inner join login using(login_id) where login_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_employee'))

	if action=='update':
		q="select * from employee where login_id='%s'"%(id)
		res=select(q)
		data['updater']=res


	if 'update' in request.form:
		first_name=request.form['first_name']
		last_name=request.form['last_name']
		phone=request.form['phone']
		place=request.form['place']
		email=request.form['email']
		qualification=request.form['qualification']
		designation=request.form['designation']
		q="update employee set first_name='%s',last_name='%s',phone='%s',place='%s',email='%s',qualification='%s',designation='%s' where login_id='%s'"%(first_name,last_name,phone,place,email,qualification,designation,id)
		update(q)
		return redirect(url_for('admin.admin_manage_employee'))

	return render_template('admin_manage_employee.html',data=data)



@admin.route("/admin_view_uploaded_files",methods=["get","post"])
def admin_view_uploaded_files():
	data={}
	q="select * from files inner join employee using(employee_id)"
	res=select(q)
	print(res)
	data['employee']=res
	return render_template('admin_view_uploaded_files.html',data=data)


@admin.route("/admin_view_feedback",methods=["get","post"])
def admin_view_feedback():
	data={}
	q="select * from feedback inner join employee using(employee_id)"
	res=select(q)
	print(res)
	data['employee']=res
	return render_template('admin_view_feedback.html',data=data)