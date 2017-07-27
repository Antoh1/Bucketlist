from app import app
import time
from flask import render_template, url_for, request, session, redirect, abort, flash


#dictionary holding user credentials
credentials={'email':'admin@gmail.com', 'password':'admin'}
#A list holding bucketlists
Blists = [{'BucketName': 'Antotiro', 'BucketDesc': 'My items in the list'}]

#defining the routes to various pages
@app.route('/')
def home():
	user = session.get('email')
	return render_template("home.html", user = user)

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
	error = None
	if request.method == 'POST':
		if (request.form['email'] in credentials) or request.form['email']=='admin@gmail.com':
			session['email'] = request.form['email']
			session['password'] = request.form['password']
			return render_template('bucketlists.html', buckets = Blists)
		else:
			flash("Wrong Signin Credentials, Kindly confirm and signin again")
			return redirect(url_for('signin'))
		    	
	return render_template("signin.html")

@app.route('/logout')
def logout():
	if session.get('email'):
	    session.pop('email')
	    session.pop('password')
	    flash("You were Logged out successfully")
	    return redirect(url_for('home'))
	flash("You are not signed in")
	return redirect(url_for('home'))    

@app.route('/signup', methods = ['GET','POST'])
def signup():
	if request.method == 'POST':
		credentials['firstName'] = request.form['FN']
		credentials['secondName'] = request.form['SN']
		credentials['email'] = request.form['EM']
		credentials['password'] = request.form['PW']
		return render_template('bucketlists.html', buckets = Blists)
	return render_template("signup.html")

@app.route('/itemsview')
def itemsview():
	return render_template("itemsview.html", cred = credentials)

@app.route('/bucketlists', methods = ['GET', 'POST'])
def bucketlist():	
	if session.get('password'):
		return render_template('bucketlists.html', buckets = Blists)
	flash('You are not authorized to view the page you tried to access, Signin first')
	return redirect(url_for('home'))					

@app.route('/create', methods = ['GET', 'POST'])
def create_bucketlist():
	if session.get('email'):
		if request.method == 'POST':
			if request.form['bn'] != '' and request.form['bd'] != '':
				Blists.append({'BucketName': request.form['bn'], 'BucketDesc': request.form['bd']})
				return render_template('bucketlists.html', buckets = Blists)
			flash('Bucketlist was not created, the fields submited were empty')
			return redirect(url_for('bucketlist'))	
		return render_template("create.html")	
	flash('You are not authorized to view the page you tried to access, Signin first')
	return redirect(url_for('home'))

@app.route('/deletebucket/<BucketName>')
def deletebucket(BucketName):
    index = 0
    for bucket in Blists:
        if BucketName == bucket['BucketName']:
            Blists.pop(index)
            flash('Bucketlist successfully deleted')
            return redirect(url_for('bucketlist', buckets = Blists))
        index+=1 