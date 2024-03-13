from flask import Blueprint, flash, render_template, request
from .models import Course,Request,db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Home page<h1>"

@views.route('/create-course', methods=['POST'])
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
    return ""

@views.route('/create-request', methods=['POST'])
def createRequest():
    if request.method == 'POST':
        username = ""
        course = ""
        new_request = Requests(username=username,course=course)
        db.session.add(new_request)
        db.session.commit()
    return "<h1>Home page<h1>"