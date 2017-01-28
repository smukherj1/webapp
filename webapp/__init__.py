from flask import Flask

import flaskapp
from views import *

app = flaskapp.app

if __name__ == '__main__':
    app.run(debug=True)
