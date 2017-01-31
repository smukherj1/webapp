from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from .views_common import *

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    login_error = None
    if form.validate_on_submit():
        User = models.User
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        # Password check. TODO: Salting
        if user is not None and\
            form.password.data != user.password:
            user = None
        if user is not None:
            login_session(user)
            return redirect('/home')
        else:
            login_error = '%s is not a valid username or the password was incorrect'%username
    return render_template('login.html', form=form, login_error=login_error)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect('/')

def login_session(user):
    session['username'] = user.username
