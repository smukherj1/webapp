from .db_handle import db

class User(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %s, %s>' % (self.username, self.email)

