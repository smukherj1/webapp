from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'foobar'

CSRFProtect(app)
