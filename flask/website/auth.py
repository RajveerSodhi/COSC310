from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import User,db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email)
        print(password)
    return render_template("login.html")

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        dob = request.form.get('dob')
        user_type = request.form.get('user_type')
        flash("Account created succesfully!", category="success")
        new_user = User(username=email,password=password,first_name=firstName,last_name=lastName,DOB=dob,user_type=user_type)
        db.session.add(new_user)
        db.session.commit()

    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))