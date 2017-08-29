from app import app
from flask import render_template, url_for, request, session, redirect, abort, flash


#dictionary holding user credentials
from users import User
NewUser = User()
#A list holding bucketlists
from buckets import Bucketlists
NewBucket = Bucketlists()

#defining the routes to various pages
@app.route('/')
def home():
    user = session.get('email')
    return render_template("home.html", user = user)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        Fname = request.form['FN']
        Sname = request.form['SN']
        email = request.form['EM']
        pwd = request.form['PW']
        userReg = NewUser.register(Fname, Sname, email, pwd)
        if userReg == "Registration Successful":
            session['email'] = request.form['EM']
            session['Fname'] = request.form['FN']
            return redirect(url_for('signin', ))
        else:
            flash('The Email is already in Use')
            return redirect(url_for('signup'))
    return render_template("signup.html")


@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        userLog = NewUser.login(email, password)
        if userLog=="Login Successful" or (email =='admin@gmail.com' and password=='12'):
            if email=='admin@gmail.com':
                session['email'] = request.form['email']
                session['Fname'] = 'Admin'
                return redirect(url_for('bucketlist'))
            else:
                session['email'] = request.form['email']
                session['Fname'] = NewUser.userInfo[email]['Fname']
                return redirect(url_for('bucketlist'))    
        else:
            flash("Wrong Signin Credentials, Kindly confirm and signin again")
            return redirect(url_for('signin'))
    return render_template("signin.html")

@app.route('/logout')
def logout():
    if session.get('email'):
        session.pop('email')
        session.pop('Fname')
        flash("You were Logged out successfully")
        return redirect(url_for('home'))
    flash("You are not signed in")
    return redirect(url_for('home'))    

@app.route('/bucketlists', methods = ['GET', 'POST'])
def bucketlist():
    if session.get('email'):
        if request.method == 'POST':
            owner = session['email']
            name = request.form['bn']
            description = request.form['bd']
            if name != '' and description != '':
                newBucket = NewBucket.create_bucket(name, owner, description)
                if newBucket=="Bucket created Successfully":
                    flash("Bucketlist created successfully")
                    return redirect(url_for('bucketlist'))
                else:
                    flash('Bucketlist not created')
                    return redirect(url_for('bucketlist'))
            else:
                flash('Bucketlist was not created, the fields submited were empty')
                return redirect(url_for('bucketlist'))
        else:
            user = NewUser.userInfo
            Blists = NewBucket.Buckets
            items = NewBucket.items
            return render_template('bucketlists.html', user=user, buckets = Blists, items = items )
    else:
        flash("You are not authorized to view the page you tried to access, Signin first")
        return redirect(url_for('home'))					

@app.route('/deletebucket/<BucketName>')
def deletebucket(BucketName=None):
    if BucketName:
        del_bucket = NewBucket.delete_bucket(BucketName)
        if del_bucket == "Bucket Successfully Deleted":
            flash('Bucketlist successfully deleted')
            return redirect(url_for('bucketlist'))
        else:
            flash("Bucketlist does not Exist")
            return redirect(url_for('bucketlist'))
    else:
        flash("Bucketlist does not Exist")
        return redirect(url_for('bucketlist'))

@app.route('/addItem/<BucketName>', methods=['GET', 'POST'])
def add_item(BucketName=None):
    if BucketName:
        item = request.form['item']
        addItem = NewBucket.add_item(BucketName, item)
        if addItem=="The item added Successfully":
            flash("Item added successfully")
            return redirect(url_for("bucketlist"))
        else:
            flash("You have not provided an Item to add")
            return redirect(url_for('bucketlist'))
    else:
        flash("The Bucketlist does not exist")
        return redirect(url_for('bucketlist'))		

