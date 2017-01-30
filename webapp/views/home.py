
from .views_common import *

@app.route('/home')
def home():
    if session.get('user_id') is None:
        return redirect('/')
    user_id = session.get('user_id')
    user = models.User.query.filter_by(id=user_id).first()
    if user is None:
        # Stale cookie?
        return redirect('/logout')
    return render_template('home.html', user=user)
