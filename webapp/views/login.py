from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired
from .views_common import *

class LoginForm(FlaskForm):
    user_id = IntegerField('UserID', validators=[DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    login_error = None
    if form.validate_on_submit():
        User = models.get('User')
        user_id = form.user_id.data
        user = User.query.filter_by(id=user_id).first()
        if user is not None:
            login_session(user)
            return redirect('/home')
        else:
            login_error = '%d is not a valid user id'%user_id
    return render_template('login.html', form=form, login_error=login_error)

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect('/')

def login_session(user):
    session['user'] = user
