from sql_connection import connect_to_database
from datetime import *


def insert_order(conn, order):
    order_id = None
    if order is not None:
        cursor = conn.cursor()
        order_query = f"INSERT INTO gs.orders (CUSTOMER_NAME, TOTAL, DATETIME) VALUES ('{
            order['customer_name']}', '{order['grand_total']}', '{order['datetime']}') RETURNING order_id"
        order_id = cursor.execute(order_query)
        order_details_query = f"INSERT INTO gs.order_details (ORDER_ID, PRODUCT_ID, QUANTITY, TOTAL_PRICE) VALUES ('{
            order_id}', '{order['order_details']['product_id']}', '{order['order_details']['quantity']}', '{order['order_details']['total_price']}')"
        cursor.executemany(order_details_query)
        conn.commit()
    return order_id


if __name__ == '__main__':
    connection = connect_to_database('postgres', 'postgres',
                                     'postgres', 'localhost', '5432')
    if connection:
        insert_order(conn=connection, order={
                     'customer_name': 'dheeraj',
                     'grand_total': 310,
                     'datetime': datetime.now(),
                     'order_details': [
                         {
                             'product_id': 1,
                             'quantity': 2,
                             'total_price': 60
                         },
                         {
                             'product_id': 3,
                             'quantity': 1,
                             'total_price': 250
                         },
                     ]})
        connection.close()
