from flask import Blueprint, flash, render_template, request
from flask_login import login_required, current_user
from .models import Course, Request, db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/create-course', methods=['GET','POST'])
def createCourse():
    if request.method == 'POST':
        course_number = request.form.get('course_number')
        course_name = request.form.get('course_name')
        course_desc = request.form.get('course_desc')
        course_limit = request.form.get('course_limit')
        teacher_id = request.form.get('teacher_id')
        new_course = Course(course_number=course_number, course_name=course_name, course_desc=course_desc, course_limit=course_limit, teacher_id=teacher_id)
        db.session.add(new_course)
        db.session.commit()
    return render_template("createCourse.html", user=current_user)

@views.route('/create-request', methods=['POST'])
def createRequest():
    if request.method == 'POST':
        username = ""
        course = ""
        new_request = Request(username=username,course=course)
        db.session.add(new_request)
        db.session.commit()
    return "<h1>Home page<h1>"