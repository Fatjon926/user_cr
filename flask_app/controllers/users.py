from flask_app import app
from flask_app.models.user import User
from flask import render_template , redirect , session , request

@app.route('/')
def index():
    users=User.get_all()

    return render_template('loginuser.html', users=users)

@app.route('/add/user')
def addUser():
    return render_template('adduser.html')

@app.route('/create/user',methods=['POST'])
def createUser():
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')