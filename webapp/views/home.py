
from .views_common import *

@app.route('/home')
def home():
    if session.get('user') is None:
        return redirect('/')
    user = session.get('user')
    return render_template('home.html', user=user)
