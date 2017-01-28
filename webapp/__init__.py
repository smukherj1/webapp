from flask import Flask
from flaskapp import app

# Load the database/models
import models
models.init(app)

# Load the views
import views
views.init(app, models.model_table)

if __name__ == '__main__':
    app.run(debug=True)
