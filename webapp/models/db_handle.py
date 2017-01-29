import os

db = None

def init(app):
    from flask_sqlalchemy import SQLAlchemy
    global db

    # Generate db path
    db_path = os.environ['HOME']
    db_path = os.path.join(db_path, 'webapp.work')
    if os.environ.get('WEBAPP_RELEASE') != None:
        db_path = os.path.join(db_path, 'release', 'database')
    else:
        db_path = os.path.join(db_path, 'debug', 'database')
    # Make directories if they don't exist
    if not os.path.isdir(db_path):
        os.makedirs(db_path)
    db_path = os.path.join(db_path, '_sqlite3.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.drop_all()
