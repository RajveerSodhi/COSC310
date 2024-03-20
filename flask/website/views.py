from flask_login import login_required, current_user
from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import db, Course, Request, Enrollment, Quiz, Essay, QuizQuestion, EssayQuestion

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
        course_name = request.form.get('course_name')
        course_desc = request.form.get('course_desc')
        course_limit = request.form.get('course_limit')
        course_code = request.form.get('course_code')
        teacher_id = request.form.get('teacher_id')
        #create the new course
        new_course = Course(course_code=course_code, course_name=course_name, course_desc=course_desc, course_limit=course_limit, teacher_id=teacher_id)
        #add the new course to the session
        db.session.add(new_course)
        # commit to save the course and get its course_id
        db.session.commit()
        #creating the new enrollment for the teacher with the new course id
        teacher_enrollment = Enrollment(user_id=teacher_id,course_id=new_course.id)
        #add the teacher's enrollment to the session
        db.session.add(teacher_enrollment)
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

# Declining Enrollment Request
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

# Individual Course Page
@views.route('/course/<int:course_id>')
def course_page(course_id):
    course = Course.query.get(course_id)
    quizzes = Quiz.query.filter_by(course_id=course_id).all()
    essays = Essay.query.filter_by(course_id=course_id).all()
    return render_template('coursePage.html', course=course, quizzes=quizzes, essays=essays)

# Page for Creating Assignment for a particular Course
@views.route('/course/<int:course_id>/createAssignment', methods=['GET','POST'])
def createAssignment(course_id):
    if request.method == 'POST':
        assignment_type = request.form.get('assignmentType')
        assignment_name = request.form.get('title')

        if assignment_type == 'quiz':
            new_quiz = Quiz(quiz_name=assignment_name, course_id=course_id)
            db.session.add(new_quiz)
            db.session.commit()

            question_keys = [key for key in request.form if key.startswith('question')]
            for question_key in question_keys:
                question_number = question_key[len('question'):]
                question_text = request.form[question_key]
                options = [request.form.get(f'option{question_number}-{i}') for i in range(1, 4)]
                quiz_question = QuizQuestion(question=question_text, quiz_id=new_quiz.id, option1=options[0], option2=options[1], option3=options[2])
                db.session.add(quiz_question)

        else:
            new_essay = Essay(essay_name=assignment_name, course_id=course_id)
            db.session.add(new_essay)
            db.session.commit()
            essay_text = None
            essay_file = None

            question_type = request.form.get('contentMethodEssay')
            if question_type == 'text':
                essay_text = request.form.get('text-entry-essay')
            elif 'file-upload-essay' in request.files:
                file = request.files['file-upload-essay']
                if file and file.filename != '':  # Check if a file has been uploaded
                    essay_file = file.read()
            
            essay_question = EssayQuestion(essay_id = new_essay.id, question_type = question_type, file_upload = essay_file, question_text = essay_text)
            db.session.add(essay_question)

        db.session.commit()
        return redirect(url_for('views.home', course_id=course_id))

    return render_template('createAssignment.html', user=current_user, course_id=course_id)

# Individual Quiz Page
@views.route('/course/<int:course_id>/quiz')
def course_page(course_id):
    return render_template('quiz.html', course_id=course_id)