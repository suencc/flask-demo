from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(120), index=True)
    ip = db.Column(db.String(120))
    posts = db.relationship('Post', backref='author', lazy='dynamic')#uselist=False ,一对一

    def __repr__(self):
        return '<User %r>' % (self.nickname  )

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    def __repr__(self):
        return '<Post %r>' % (self.body)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address', backref='person',
                                lazy='dynamic')

class Address(db.Model):
    __tablename__ = "user_address"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class ValidateHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    identify = db.Column(db.String(120), index=True)
    mobileno = db.Column(db.String(225), index=True)
    court = db.Column(db.Boolean)
    overdueBlack = db.Column(db.Boolean)
    p2pBlack = db.Column(db.Boolean)
    personalBlack = db.Column(db.Boolean)

    addtime = db.Column(db.DateTime)
    exptime = db.Column(db.DateTime)#有效时间
    def __repr__(self):
        return '<User %r%r>' % (self.name, self.exptime )