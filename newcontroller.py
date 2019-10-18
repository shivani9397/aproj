from flask_basics.dbconfig import app
from flask import request,render_template
from flask_basics.model import Product
from flask_basics.productser import ProductServiceImpl

service = ProductServiceImpl()

@app.route("/welcome/")
def landing_page():
    #return 'welcome to product app...!'
    return render_template('product.html',products = service.get_all_products(),dbprod=dummy_product())
#/save
#http://localhost:5000/save -- will work
#http://localhost:5000/save/-- will not work

#/save/
#http://localhost:5000/save -- will work
#http://localhost:5000/save/-- will work

def dummy_product():
    return Product(pid=0, pname='', pven='', pprice=0.0, pcat='', pqty=0)



@app.route('/save/',methods=['POST'])
def persist_product_info():
    print('persist info ...called...!',type(request.form['pid']),request.form['pid'])
    if int(request.form['pid'])>0:
        prod = Product(pid=int(request.form['pid']),
                       pname=request.form['pname'],
                       pven=request.form['pven'],
                       pprice=float(request.form['pprice']),
                       pcat=request.form['pcat'],
                       pqty=int(request.form['pqty']))
        confirmation=service.update_product(prod)
    else:
        prod= Product(pname=request.form['pname'],
                    pven=request.form['pven'],
                    pprice=float(request.form['pprice']),
                    pcat=request.form['pcat'],
                    pqty=int(request.form['pqty']))
        confirmation = service.add_product(prod)
    return  render_template('product.html',dbprod=dummy_product(),
                            msg=confirmation,products = service.get_all_products())


@app.route('/product/edit/<int:prodId>')
def edit_product(prodId):
    dbproduct = service.get_product(prodId)

    return render_template('product.html',
                           msg='Edit method Invoked,'+str(prodId),
                           products=service.get_all_products(),
                           dbprod=dbproduct)

@app.route('/product/delete/<int:prodId>')
def delete_product(prodId):
    service.delete_product(prodId)
    return render_template('product.html',dbprod=dummy_product(),
                           msg='Delete Method Invokved,'+str(prodId), products=service.get_all_products())

if __name__ == '__main__':
    app.run(debug=True)