from flask import Flask, request, jsonify
from sql_connection import connect_to_database
from products_dao import *

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


if __name__ == '__main__':
    app.run(port=5000)
