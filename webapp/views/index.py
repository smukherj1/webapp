
from views_common import *

@app.route('/')
def index():
    if session.get('logged_in') is None:
        return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return __app.send_static_file('favicon.ico')
