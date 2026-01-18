from flask import (
    Flask, render_template, request,
    redirect, url_for, flash, session
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager, UserMixin,
    login_user, logout_user,
    login_required, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
import string
import random

# --------------------
# App Configuration
# --------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --------------------
# Flask-Login Setup
# --------------------
login_manager = LoginManager()
login_manager.login_view = 'login'  # type: ignore
login_manager.init_app(app)

# --------------------
# Database Models
# --------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    urls = db.relationship('URL', backref='user', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# --------------------
# User Loader
# --------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --------------------
# Helper Function
# --------------------
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
def generate_unique_short_code():
    while True:
        code = generate_short_code()
        if not URL.query.filter_by(short_code=code).first():
            return code

# --------------------
# Routes
# --------------------

# Home – Guest + Logged-in
@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None

    # Initialize guest session storage
    if 'guest_urls' not in session:
        session['guest_urls'] = []

    if request.method == 'POST':
        original_url = request.form.get('url')

        if not original_url:
            flash('Please enter a valid URL')
            return redirect(url_for('home'))

        short_code = generate_unique_short_code()
        short_url = short_code

        # Logged-in user → save to DB
        if current_user.is_authenticated:
            new_url = URL(
                original_url=original_url,
                short_code=short_code,
                user_id=current_user.id
            )
            db.session.add(new_url)
            db.session.commit()

        # Guest user → save to session
        else:
            session['guest_urls'].insert(0, {
                'original_url': original_url,
                'short_code': short_code
            })
            session.modified = True

    # Fetch recent URLs
    if current_user.is_authenticated:
        recent_urls = (
            URL.query
            .filter_by(user_id=current_user.id)
            .order_by(URL.id.desc())
            .limit(5)
            .all()
        )
    else:
        recent_urls = session.get('guest_urls', [])[:5]

    return render_template(
        'home.html',
        short_url=short_url,
        recent_urls=recent_urls
    )

# Redirect Short URL (Public)
@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        return redirect(url_entry.original_url)
    return "URL not found", 404

# Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if len(username) < 5 or len(username) > 9:
            flash('Username must be between 5 to 9 characters long')
            return redirect(url_for('signup'))

        if User.query.filter_by(username=username).first():
            flash('This username already exists')
            return redirect(url_for('signup'))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Signup successful! Please login.')
        return redirect(url_for('login'))

    return render_template('signup.html')


# Login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user)
        session.pop('guest_urls', None)
        flash('Login successful')
        return redirect(url_for('home'))

    return render_template('login.html')




# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('home'))

# --------------------
# Run App
# --------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
