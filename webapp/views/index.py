
from .views_common import *

@app.route('/')
def index():
    if session.get('username') is None:
        return render_template('index.html')
    else:
        return redirect('/home')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/reset_db')
def reset_db():
    # Use for unit testing only
    if os.environ.get('WEBAPP_UNIT_TEST') != None:
        models.db().drop_all()
        models.db().create_all()
        session.clear()
        return 'OK'
    else:
        # Thou hast been forbidden
        flask.abort(403)
