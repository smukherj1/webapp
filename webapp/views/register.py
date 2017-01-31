from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email
from .views_common import *
from .login import login_session

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        db = models.db()
        user = models.Account.query.filter_by(username=form.username.data).first()
        if user is not None:
            return render_template('register.html', 
                    form=form, 
                    register_error='Sorry username %s is taken'%user.username)
        else:
            # User doesn't exist. Commit user details to database and redirect to home
            user = models.Account(form.username.data, form.password.data, form.email.data)
            db.session.add(user)
            db.session.commit()
            login_session(user)
            return redirect('/home')
    else:
        return render_template('register.html', form=form, register_error=None)
