from flask import Flask
from flask_serialize import FlaskSerializeMixin
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost:5432/FlaskAppDatabase"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
FlaskSerializeMixin.db = db


class Administrator(db.Model, FlaskSerializeMixin):
    administrator_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    super_admin = db.Column(db.Boolean, default=False)


class Seller(db.Model, FlaskSerializeMixin):
    seller_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(128), nullable=False)


class Car(db.Model, FlaskSerializeMixin):
    car_id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.seller_id'))
    make = db.Column(db.String(128), nullable=False)
    model = db.Column(db.String(128), nullable=False)
    first_registration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    fuel = db.Column(db.String(128), nullable=False)


if __name__ == '__main__':
    manager.run()
