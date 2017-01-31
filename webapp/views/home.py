
from .views_common import *

@app.route('/home')
def home():
    if session.get('username') is None:
        return redirect('/')
    username = session.get('username')
    user = models.User.query.filter_by(username=username).first()
    if user is None:
        # Stale cookie?
        return redirect('/logout')
    return render_template('home.html', user=user)
