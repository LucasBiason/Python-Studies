from market import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'User {self.username}'

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'



''' # NOTES:
from market import db
from market.models import User, Item

u1 = User(username='jsc', password_hash='123456', email_address='jsc@jsc.com')
item1.owner = u1
db.session.add(u1)
db.session.commit()

item1 = Item(name="IPhone 10", price=500, barcode='8273647839', description='desc iphone')
item2 = Item(name="Laptop", price=600, barcode='8279232439', description='desc laptop')
db.session.add(item1)
db.session.add(item2)
db.session.commit()

item1.owner = u1.id
db.session.add(item1)
db.session.commit()
# Agora sera acessivel via: item1.owned_user


(!) https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html

'''