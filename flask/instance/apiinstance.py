from flask_login import login_required, current_user
from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import Course, Request, Enrollment, User, db
from .forms import CourseForm, RequestForm

views = Blueprint('views', __name__)

# Home route
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)



# Route to create a new course
@views.route('/create-course', methods=['GET','POST'])
def create_course():
    form = CourseForm()
    if form.validate_on_submit():
        new_course = Course(
            course_code=form.course_code.data,
            course_name=form.course_name.data,
            course_desc=form.course_desc.data,
            course_limit=form.course_limit.data,
            teacher_id=current_user.id
        )
        db.session.add(new_course)
        db.session.commit()
        flash('Course created successfully', 'success')
        return redirect(url_for('views.create_course'))
    return render_template("create_course.html", user=current_user, form=form)




# Route to create a new request
@views.route('/create-request', methods=['POST'])
@login_required
def create_request():
    form = RequestForm()
    if form.validate_on_submit():
        new_request = Request(
            user_id=current_user.id,
            course_id=form.course_id.data
        )
        db.session.add(new_request)
        db.session.commit()
        flash('Request created successfully', 'success')
        return redirect(url_for('views.display_courses'))
    flash('Error creating request', 'danger')
    return redirect(url_for('views.display_courses'))





# Route to display available courses for enrollment
@views.route('/enroll-courses')
@login_required
def display_courses():
    courses = Course.query.all()
    return render_template('enroll_course.html', user=current_user, courses=courses)




# Route to display requests made by users
@views.route('/requests')
@login_required
def display_requests():
    requests = Request.query.all()
    return render_template('accept_course.html', requests=requests)





# Route to accept a request
@views.route('/accept-request', methods=['POST'])
@login_required
def accept_request():
    user_id = request.form.get('user_id')
    course_id = request.form.get('course_id')
    new_enrollment = Enrollment(user_id=user_id, course_id=course_id)
    if new_enrollment:
        db.session.add(new_enrollment)
        db.session.commit()
        request_to_delete = Request.query.filter_by(user_id=user_id, course_id=course_id).first()
        db.session.delete(request_to_delete)
        db.session.commit()
        flash('Request accepted successfully', 'success')
    else:
        flash('Error accepting request', 'danger')
    return redirect(url_for('views.display_requests'))





# Route to decline a request
@views.route('/decline-request', methods=['POST'])
@login_required
def decline_request():
    user_id = request.form.get('user_id')
    course_id = request.form.get('course_id')
    request_to_delete = Request.query.filter_by(user_id=user_id, course_id=course_id).first()
    if request_to_delete:
        db.session.delete(request_to_delete)
        db.session.commit()
        flash('Request declined successfully', 'success')
    else:
        flash('Error declining request', 'danger')
    return redirect(url_for('views.display_requests'))

# Add more routes, views, models, forms, etc. to extend the code...




# Route to view user profile
@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)




# Route to update user profile
@views.route('/update-profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.commit()
        flash('Profile updated successfully', 'success')
        return redirect(url_for('views.profile'))
    return render_template('update_profile.html', form=form)





# Route to view all users
@views.route('/users')
@login_required
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

def profile():
    return render_template('profile.html', user=current_user)





# Route to update user profile
@views.route('/update-profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.commit()
        flash('Profile updated successfully', 'success')
        return redirect(url_for('views.profile'))
    return render_template('update_profile.html', form=form)




# Route to view all users
@views.route('/users')
@login_required
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)





# Route to generate dummy data
@views.route('/generate-data')
@login_required
def generate_data():
    # Generate dummy users
    for _ in range(10):
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        email = f"{username}@example.com"
        new_user = User(username=username, email=email)
        db.session.add(new_user)
    db.session.commit()

    # Generate dummy courses
    for _ in range(20):
        course_code = ''.join(random.choices(string.ascii_uppercase, k=4))
        course_name = ''.join(random.choices(string.ascii_uppercase + ' ', k=10))
        course_desc = ''.join(random.choices(string.ascii_lowercase + ' ', k=20))
        course_limit = random.randint(10, 50)
        teacher_id = random.randint(1, 10)
        new_course = Course(course_code=course_code, course_name=course_name, course_desc=course_desc, course_limit=course_limit, teacher_id=teacher_id)
        db.session.add(new_course)
    db.session.commit()

    flash('Dummy data generated successfully', 'success')
    return redirect(url_for('views.home'))





# Error handling for 404 page not found
@views.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404





# Error handling for 500 internal server error
@views.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

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





@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

db = SQLAlchemy()
DB_NAME = "database.db"





def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gvfvsvf'
    app.config["SQLALCHEMY_DATABASE_URI"]= f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    # app.register_blueprint(auth, url_prefix= '/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User

    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists('website/'+DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")






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
    
    
    
from website import create_app
from flask import app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

 