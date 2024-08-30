from flask import Flask, request, jsonify
from sql_connection import connect_to_database
from products_dao import *
from orders_dao import *
from uom_dao import *
import json

app = Flask(__name__)

connection = connect_to_database(
    'postgres', 'postgres', 'postgres', 'localhost', '5432')


@app.route('/getProducts', methods=['GET'])
def get_all_products():
    global connection
    products = get_products(conn=connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def del_product():
    return_id = delete_product(
        conn=connection, product_id=request.form['product_id'])
    response = jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def add_product():
    request_payload = json.loads(request.form['data'])
    return_id = insert_product(conn=connection, product=request_payload)
    response = jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def create_order():
    request_payload = json.loads(request.form['data'])
    return_id = insert_order(conn=connection, order=request_payload)
    response = jsonify({'order_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getUOM', methods=['GET'])
def get_all_uoms():
    uoms = get_uoms(conn=connection)
    response = jsonify(uoms)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(port=5000)
