from flask import Flask

from flaskapp import app
from views import *

if __name__ == '__main__':
    app.run(debug=True)
