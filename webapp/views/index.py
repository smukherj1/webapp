
from .views_common import *

@app.route('/')
def index():
    if session.get('user') is None:
        return render_template('index.html')
    else:
        return redirect('/')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')
