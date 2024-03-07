from .  import db
import flask
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
    grades = db.relationship('Grade', backref='user')

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class Student(User):  # Assuming inheritance from User
    __tablename__ = 'students'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    # Relationship for many-to-many with Course
    courses = db.relationship('Course', secondary='student_courses', backref='students')

# Association table for Student-Course many-to-many relationship
student_courses = db.Table('student_courses',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    # Relationships
    courses = db.relationship('Course', backref='teacher')

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(150))
    course_limit = db.Column(db.Integer)
    course_desc = db.Column(db.String(1000))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    # Relationships
    sections = db.relationship('Section', backref='course')
    assignments = db.relationship('Assignment', backref='course')

class Section(db.Model):
    __tablename__ = 'sections'
    id = db.Column(db.Integer, primary_key=True)
    course_section = db.Column(db.Integer)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    scored_points = db.Column(db.Integer)
    max_points = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

class Assignment(db.Model):
    __tablename__ = 'assignments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    due_date = db.Column(db.DateTime)
    total_points = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(1000))
    # Foreign Key - Each Question belongs to one Assignment
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))




