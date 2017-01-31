import os

db = None

def init(app):
    from flask_sqlalchemy import SQLAlchemy
    global db

    db_path = 'postgresql://postgres:password@/'
    if os.environ.get('WEBAPP_RELEASE') != None:
        db_path += 'webapp'
    else:
        db_path += 'webapp_test'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.drop_all()
