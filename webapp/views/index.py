from flaskapp import app


@app.route('/')
def index():
    return '<html><title>Hello!</title><body><h1>Hello!</h1>Howdy! How ya doin?</body></html>'

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')
