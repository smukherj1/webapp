
__app = None

def index():
    return '<html><title>Hello!</title><body><h1>Hello!</h1>Howdy! How ya doin?</body></html>'

def favicon():
    return __app.send_static_file('favicon.ico')

def init(app):
    global __app
    __app = app
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/favicon.ico', 'favicon', favicon)
