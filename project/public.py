from flask import *
from database import *

public=Blueprint("public",__name__)

@public.route('/')
def home():
	return render_template('home.html')

@public.route("/login",methods=["get","post"])
def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)	
		print(res)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.admin_home'))
		else:
			flash("INVALID USERNAME OR PASSWORD")
			return redirect(url_for('admin.admin_home'))
	return render_template('login.html')