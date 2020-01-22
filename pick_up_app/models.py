from pick_up_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(15), nullable=False, default='security')
    house_address = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(15), nullable=True)
    password = db.Column(db.String(15), nullable=False)


    def __repr__(self):
        return f"User({self.full_name}, {self.position})"

