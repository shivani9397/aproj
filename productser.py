from abc import ABC,abstractmethod
from flask_basics.model import Product
from flask_basics.productdao import ProductDAOImpl
class ProductService(ABC):

    @abstractmethod
    def add_product(self,prod):
        pass
    @abstractmethod
    def get_product(self,pid):
        pass
    @abstractmethod
    def get_all_products(self):
        pass
    @abstractmethod
    def update_product(self,prod):
        pass
    @abstractmethod
    def delete_product(self,pid):
        pass

class ProductServiceImpl(ProductService):
    impl = None

    def __init__(self):
        ProductDAOImpl.impl = ProductDAOImpl()

    def add_product(self, prod):
        returnval = ""
        if not type(prod)==Product:
            returnval='Invalid Product'
       # elif prod.pid<=0 or not type(prod.pid)==int:
       #     returnval='INvalid product Id'
        elif prod.pprice<500:
            returnval='Price shud be atleast 500'
        elif self.get_product(prod.pid):
            returnval='Already Exist...!'
        else:
            ProductDAOImpl.impl.insert_product(prod)
            returnval='Product Added Successfully....!'

        return returnval

    def get_product(self, pid):
        if type(pid)==int and pid>0:
            product= ProductDAOImpl.impl.fetch_product(pid)
            if product:
                return product

    def get_all_products(self):
        products = ProductDAOImpl.impl.fetch_all_products()
        return products
    def update_product(self, prod):
        if type(prod)==Product:
            dbproduct= self.get_product(prod.pid)
            if dbproduct:
                ProductDAOImpl.impl.modify_product(prod)
                return 'Product updated Successfully....!'
            else:
                return "Product not avaiable...so cannot update!"
        else:
            return 'Invalid product'

    def delete_product(self, pid):
        if type(pid)==int and pid>0:
            dbproduct= self.get_product(pid)
            if dbproduct:
                ProductDAOImpl.impl.remove_product(pid)
                print('Product Deleted Successfully...!')
            else:
                print("Product not avaiable...so cannot delete!")
        else:
            print('Invalid product id..cannot delete')


