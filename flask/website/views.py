from flask_login import login_required, current_user
from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import Course, Request, Enrollment, db

views = Blueprint('views', __name__)

# Home Page (Dashboard)
@views.route('/')
@login_required
def home():
    enrolled_courses = Course.query.join(Enrollment).filter(Enrollment.user_id == current_user.id).all()
    return render_template("home.html", user=current_user, enrolled_courses=enrolled_courses)

# Page for Creating a New Course - Admin
@views.route('/create-course', methods=['GET','POST'])
def createCourse():
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        course_name = request.form.get('course_name')
        course_desc = request.form.get('course_desc')
        course_limit = request.form.get('course_limit')
        teacher_id = request.form.get('teacher_id')
        new_course = Course(course_code=course_code, course_name=course_name, course_desc=course_desc, course_limit=course_limit, teacher_id=teacher_id)
        db.session.add(new_course)
        db.session.commit()
    return render_template("createCourse.html", user=current_user)

# Creating Enrollment Request
@views.route('/create-request', methods=['POST'])
def createRequest():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        course_id = request.form.get('course_id')
        new_request = Request(user_id=user_id, course_id=course_id)
        db.session.add(new_request)
        db.session.commit()
    return redirect(url_for('views.display_courses'))

# Page for Enrolling in a New Course - Student
@views.route('/enroll-courses')
def display_courses():
    courses = Course.query.all()
    return render_template('enrollCourse.html', user=current_user, courses=courses)

# Page for Accepting Student Request - Admin
@views.route('/requests')
def display_requests():
    requests = Request.query.all()
    return render_template('acceptCourse.html', requests=requests)

# Accepting Enrollment Request
@views.route('/accept-request', methods=['POST'])
def acceptRequest():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        course_id = request.form.get('course_id')
        new_enrolment = Enrollment(user_id=user_id, course_id=course_id)
        if new_enrolment:
            db.session.add(new_enrolment)
            db.session.commit()
            request_to_delete = Request.query.filter_by(user_id=user_id, course_id=course_id).first()
            db.session.delete(request_to_delete)
            db.session.commit()
        
    return redirect(url_for('views.display_requests'))

# Declining Enrollemnt Request
@views.route('/decline-request', methods=['POST'])
def declineRequest():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        course_id = request.form.get('course_id')
        request_to_delete = Request.query.filter_by(user_id=user_id, course_id=course_id).first()
        if request_to_delete:
            db.session.delete(request_to_delete)
            db.session.commit()
    return redirect(url_for('views.display_requests'))

@views.route('/course/<int:course_id>')
def course_page(course_id):
    course = Course.query.get(course_id)
    return render_template('coursePage.html', course=course)