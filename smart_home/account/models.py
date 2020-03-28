from ..app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return "User('{0}', '{1}', '{2}')".format(self.username,
                                                  self.email,
                                                  self.image_file)
