from flask_basics.dbconfig import *

class Product(db.Model):
    __tablename__ ='PRODUCT_INFO'
    pid = db.Column('PROD_ID',db.Integer, primary_key=True)
    pname = db.Column('PROD_NAME',db.String(80),nullable=False)
    pcat = db.Column('PROD_CAT', db.String(80), unique=True, nullable=False)
    pprice = db.Column('PROD_PRICE', db.Float(),default=0.0)
    pven = db.Column('PROD_VEN', db.String(80), nullable=False)
    pqty = db.Column('PROD_QTY', db.Integer)

    def __str__(self):
        if self.__dict__.__contains__('_sa_instance_state'):
            self.__dict__.pop('_sa_instance_state')
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)

