from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired
from views_common import *

class LoginForm(FlaskForm):
    user_id = IntegerField('UserID', validators=[DataRequired()])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'ooo'
    return render_template('login.html', form=form)
