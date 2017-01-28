from flask import Flask
from flaskapp import app

import views
views.init(app)

if __name__ == '__main__':
    app.run(debug=True)
