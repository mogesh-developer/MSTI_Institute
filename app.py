from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this!
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_auth_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    applied_courses = db.Column(db.Text, default='')  # Store as comma-separated values
    
    def get_applied_courses_list(self):
        return [c.strip() for c in self.applied_courses.split(',') if c.strip()]
    
    def add_course(self, course_name):
        courses = self.get_applied_courses_list()
        if course_name not in courses:
            courses.append(course_name)
            self.applied_courses = ','.join(courses)
    
    def remove_course(self, course_name):
        courses = self.get_applied_courses_list()
        if course_name in courses:
            courses.remove(course_name)
            self.applied_courses = ','.join(courses)

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False) 


@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')  # Add a template or change as needed


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username already exists!')
            return redirect(url_for('register'))

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')
    


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            return redirect(url_for('dashboard'))

        else:
            flash('Invalid credentials.')
            return redirect(url_for('index.html'))

    return render_template('login.html')
@app.route('/user_dashboard')
def user_dashboard():
    if 'username' not in session:
        flash('Please log in to access the dashboard.')
        return redirect(url_for('login'))

    user = User.query.filter_by(username=session['username']).first()
    applied_courses = user.get_applied_courses_list() if user else []

    return render_template('dashboard.html', username=session['username'], applied_courses=applied_courses)


# SECRET admin registration route (not linked in UI)
@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    secret_key = request.args.get('key')  # Only accessible with correct ?key=XYZ

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if Admin.query.filter_by(username=username).first():
            flash("Admin already exists.")
            return redirect(url_for('admin_login'))
        hashed_pw = generate_password_hash(password)
        new_admin = Admin(username=username, password=hashed_pw)
        db.session.add(new_admin)
        db.session.commit()
        flash("Admin registered successfully. Please login.")
        return redirect(url_for('admin_login'))
    return render_template('admin_register.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        admin = Admin.query.filter_by(username=uname).first()
        if admin and check_password_hash(admin.password, pwd):
            session['is_admin'] = True
            session['admin_user'] = uname
            return redirect(url_for('admin_dashboard'))
        flash('Invalid admin credentials')
    return render_template('admin_login.html')


@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('is_admin'):
        flash('Unauthorized access')
        return redirect(url_for('admin_login'))
    all_users = User.query.all()
    user_list = [{'username': u.username, 'applied_courses': u.get_applied_courses_list()} for u in all_users]
    return render_template('admin_dashboard.html', users=user_list)

@app.route('/admin/logout')
def admin_logout():
    session.pop('is_admin', None)
    flash('Admin logged out.')
    return redirect(url_for('admin_login'))


@app.route('/remove_course', methods=['POST'])
def remove_course():
    if 'username' not in session:
        flash('You must be logged in.')
        return redirect(url_for('login'))

    course_to_remove = request.form.get('course_name')
    username = session['username']

    user = User.query.filter_by(username=username).first()
    if user:
        user.remove_course(course_to_remove)
        db.session.commit()

    flash(f'Removed course: {course_to_remove}')
    return redirect(url_for('user_dashboard'))


@app.route('/apply_course', methods=['POST'])
def apply_course():
    if 'username' not in session:
        flash('Please log in to apply.')
        return redirect(url_for('login'))

    course_title = request.form.get('course_title')
    username = session['username']

    # Avoid duplicates
    user = User.query.filter_by(username=username).first()
    if user:
        applied = user.get_applied_courses_list()
        if course_title not in applied:
            user.add_course(course_title)
            db.session.commit()
            flash(f'You have successfully applied for: {course_title}')
        else:
            flash(f'You already applied for: {course_title}')

    return redirect(url_for('dashboard'))



@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    flash('You must be logged in to view the dashboard.')
    return redirect(url_for('login'))

@app.route('/dhm.html')
def dhm():
    return render_template('dhm.html')

@app.route('/dgda')
def dgda_course():
    return render_template('dgda.html')

@app.route('/dxrt')
def dxrt_course():
    return render_template('dxrt.html')

@app.route('/dmlta')
def dmlta_course():
    return render_template('dmlta.html')

@app.route('/dna')
def dna():
    return render_template('dna.html')

@app.route('/dhmct')
def dhmct():
    return render_template('dhmct.html')

@app.route('/dpsm')
def dpsm():
    return render_template('dpsm.html')

@app.route('/dct')
def dct():
    return render_template('dct.html')

@app.route('/difp')
def difp():
    return render_template('difp.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.')
    return redirect(url_for('login'))


# Create database tables before first request
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
