import flask
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique = True) #email for username
    password=db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    DOB =  db.Column(db.String(150))
    user_type = db.Column(db.String(50))
    
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.Integer(), unique = True)
    course_name = db.Column(db.String(150))
    course_limit = db.Column(db.Integer)
    course_desc = db.Column(db.String(1000))
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
class Request(db.Model, UserMixin):
    __tablename__ = 'requests'
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    
class Enrollment(db.Model, UserMixin):
    __tablename__ = 'enrollments'
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))



# class Grade(db.Model):
#     __tablename__ = 'grades'
#     id = db.Column(db.Integer, primary_key=True)
#     scored_points = db.Column(db.Integer)
#     max_points = db.Column(db.Integer)
#     student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

# class Assignment(db.Model):
#     __tablename__ = 'assignments'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150))
#     due_date = db.Column(db.DateTime)
#     total_points = db.Column(db.Integer)
#     description = db.Column(db.String(1000))
#     course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
#     section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))

# class Question(db.Model):
#     __tablename__ = 'questions'
#     id = db.Column(db.Integer, primary_key=True)
#     desc = db.Column(db.String(1000))
#     # Foreign Key - Each Question belongs to one Assignment
#     assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))




