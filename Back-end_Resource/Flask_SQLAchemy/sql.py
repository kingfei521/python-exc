from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from loguru import logger
import pymysql
pymysql.install_as_MySQLdb()
import os

# 初始化
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
"""
可以链接多种flask支持的数据库此处仅仅掩饰两个

"""
## sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

## mysql （testsql数据数据库需要提前创建好）
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/testingdb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty,):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


"""
\* 模型定义完成之后，进入cd Flsk_SQLAchemy目录下， 调用python
\* from sql.py import db后然后执行db.create_all()表就在数据库创建好了
\* 接着就可以写业务代码 运行服务，调试修改了
"""


# Create a Product
@app.route('/product', methods=["POST"])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# Get All products
@app.route('/product', methods=["GET"])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return products_schema.jsonify(result)


# Get one product
@app.route('/product/<id>', methods=["GET"])
def get_product(id):
    product = Product.query.get(id)
    logger.debug(product_schema.jsonify(product).data)
    return product_schema.jsonify(product)


# Update product
@app.route('/product/<id>', methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()
    return product_schema.jsonify(product)


# delete product
@app.route('/product/<id>', methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)