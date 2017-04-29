from app import db

class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self): #__repr__ tells python how to print objects of this class
        return '<User%r>' % (self.nickname)
