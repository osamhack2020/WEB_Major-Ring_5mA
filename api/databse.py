from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///major-ring.db',echo=True)
meta = MetaData()

users = Table(
    'users', meta,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('major',String)
)


class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(100), default='default.png')

    posts = db.relationship('Post', backref='author', lazy=True)


def __init__(self, username, email, password, **kwargs):
    self.username = username
    self.email = email

    self.set_password(password)


def __repr__(self):
    return f"<User('{self.id}', '{self.username}', '{self.email}')>"


def set_password(self, password):
    self.password = generate_password_hash(password)


def check_password(self, password):
    return check_password_hash(self.password, password)


user = User(username='user', email='user@blog.com', password='password')
db.session.add(user)
db.session.commit()

print(user)