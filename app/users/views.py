from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db
from flask_login import login_user, current_user, logout_user, login_required


from app.users.model import User

from app.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)

# register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        
        user = User(name=sanitize_input(form.name.data),
                    phone=sanitize_input(form.phone.data),
                    email=sanitize_input(form.email.data),
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/registered', methods=['GET'])
def registered():
    return render_template('registered.html')

# LIST
@users.route('/list')
@login_required
def list():
    # Grab a list of users from database.
    users = User.query.all()
    return render_template('list_users.html', users=users)

@users.route('/<int:user_id>/delete', methods=['GET', 'POST'])
def delete_user(user_id):

    user = User.query.get_or_404(user_id)
    
    db.session.delete(user)
    db.session.commit()
    flash('User Deleted')
    return redirect(url_for('users.list'))

@users.route('/login',methods=['GET','POST'])
def login():
    error = None
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        
        if user is not None and user.check_password(form.password.data) :
            login_user(user)
            flash('Log in Success!')
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('index')
            return redirect(next)
        else: 
            error = 'Invalid credentials'
            print('credetials wrong')

            
    return render_template('login.html', form=form, error=error)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

def sanitize_input(raw: str) -> str:
    CLEAR = ""
    return raw.replace("'", CLEAR).replace("--", CLEAR).replace(";", CLEAR).replace("%", CLEAR)