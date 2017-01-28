db = None

def init(app):
    from flask_sqlalchemy import SQLAlchemy
    global db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///_webapp_sqlite3.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.drop_all()
    db.create_all()