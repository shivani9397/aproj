from flask_basics.model import Product
from flask_basics.dbconfig import db
from flask_basics.productser import ProductServiceImpl
if __name__ == '__main__':
    service = ProductServiceImpl()
    p1= Product(pid=10,pname='TeleVision',pven='FLip',pprice=500.3,pcat='A',pqty=23)
    #service.add_product(p1)
    service.get_all_products()
    #print(service.get_product(10))
    #service.update_product(p1)
    #service.delete_product(10)


