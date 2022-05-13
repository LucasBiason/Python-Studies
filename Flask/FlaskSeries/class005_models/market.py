from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self): # Similar to __str__
        return f'Item {self.name}'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


''' # NOTES:
from market import db
db.create_all() --> To create database

from market import Item
item1 = Item(name="IPhone 10", price=500, barcode='8273647839', description='desc iphone')
db.session.add(item1)
db.session.commit()

Item.query.all()

item2 = Item(name="Laptop", price=600, barcode='8279232439', description='desc laptop')
db.session.add(item2)
db.session.commit()

# Save this -> Item.query.filter_by(price=500)
# DO NOT -> Item.query.filter(Item.price=500)
# DO NOT -> db.session.query(Item.id).filter(Item.price == 500).all()
# DO NOT -> Item.query.with_entities(Item.id, Item.price).filter(Item.price >= 500).all()

(!) https://docs.sqlalchemy.org/en/14/orm/loading_columns.html

** scalar() returns the first element of the first result or None,
if no rows were found. It raises MultipleResultsFound exception for multiple rows.

Item.query.filter_by(price=500).scalar()

** load_only() indicates that only the given column-based attributes of an entity
should be loaded and all others, expect the identity, will be deferred.
If you do need the whole User model object later, this can be the way to go.
In that case your original query has to change to:

Item.query.filter_by(price=500).options(db.load_only("id"))

** one() returns exactly one result or raises an exception (0 or more than 1 result).
If you accept None as a valid return value for "no user found", use one_or_none().

Item.query.filter_by(price=500).one()
Item.query.filter_by(price=500).one_or_none()

** defer() columns can be marked as “deferred” at query time,
column will not load until accessed.

Item.query.filter_by(price=500).options(db.defer("barcode"))


(!) https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html

'''