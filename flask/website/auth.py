from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import User,db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if (user.password==password):
                print("Logged in Successfully!")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                print("Incorrect password, please try again.")
        else:
            print("Username does not exist!")

    return render_template("login.html", user=current_user)

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
        login_user(new_user, remember=True)
        return redirect(url_for('views.home'))
        
    return render_template("signup.html", user=current_user)

@auth.route('/editDetails', methods=['GET', 'POST'])
@login_required
def edit_details():
    if request.method == 'POST':
        # Retrieve the updated details from the form
        email = request.form.get('email')
        user = User.query.filter_by(username=email).first()
        if user:
            user.password = request.form.get('password')
            user.first_name = request.form.get('firstName')
            user.last_name = request.form.get('lastName')
            user.DOB = request.form.get('dob')
            db.session.commit()
            flash("Details updated successfully!", category="success")
            return redirect(url_for('views.home'))
        else:
            flash("User not found!", category="error")
           


    return render_template("EditDetails.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
