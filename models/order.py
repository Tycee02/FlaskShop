from .db import db

class Order(db.Model):
    """start order class to collect the product of the customer"""
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    costumer_id = db.Column(db.Integer, db.ForeignKey('costumers.id'), nullable=False)

    products = db.relationship('ProductOrder', back_populates='order')
