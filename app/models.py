from app import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), index = True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<User {}>'.format(self.name)


class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    todo = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text,nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))

    def __repr__(self):
        return '<Todo {}>'.format(self.todo)
    
class Product(db.Model):
    kode = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nameProduct  = db.Column(db.String(140), nullable=False)
    descProduct = db.Column(db.String(140), nullable=False)
    price = db.Column(db.BigInteger, nullable=False)
    stock = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Product {}>'.format(self.todo)

class CategoryProduct(db.Model):
    idCategory = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nameCategory  = db.Column(db.String(140), nullable=False)
    descCategory = db.Column(db.String(140), nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    kdProduct = db.Column(db.BigInteger, db.ForeignKey(Product.kode))
    
    def __repr__(self):
        return '<CategoryProduct {}>'.format(self.todo)