from flask import Flask
from flask_wtf.csrf import CSRFProtect

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'foobar'
CSRFProtect(app)

# Load the database/models
from . import models
models.init(app)

# Load the views
from . import views
views.init(app, models.model_table)
