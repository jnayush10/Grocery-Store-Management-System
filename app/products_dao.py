from sql_connection import connect_to_database

list_of_products = []


def get_products(conn):
    '''gets the complete list of products available in grocery store.
    Args:
      conn: The psycopg2 connection object.

    Returns:
      list of products available in the grocery
    '''
    query = 'SELECT p.product_id, p.name, u.uom_id, u.uom_name, p.price_per_unit FROM gs.products as p inner join gs.uom as u on p.uom_id = u.uom_id ORDER BY product_id ASC'

    with conn.cursor() as cur:
        cur.execute(query)
        products = cur.fetchall()

    for (product_id, name, unit_of_measure_id, unit_of_measure, price_per_unit) in products:
        list_of_products.append({
            'product_id': product_id,
            'product_name': name.strip(),
            'uom_id': unit_of_measure_id,
            'uom_name': unit_of_measure.strip(),
            'price_per_unit': price_per_unit
        })

    return list_of_products


def insert_product(conn, product):
    '''insert a new product to the inventory of grocery store
    Args:
      conn: The psycopg2 connection object.
      product: A dictionary object with details of new product

    Returns:
      None
    '''
    if product is not None:
        query = f"INSERT INTO gs.products (NAME, UOM_ID, PRICE_PER_UNIT) VALUES ('{
            product['product_name']}', '{product['uom_id']}', '{product['price_per_unit']}')"
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


def delete_product(conn, product_id):
    '''delete a product from the inventory of grocery store
    Args:
      conn: The psycopg2 connection object.
      product_id: The product id of the product to be deleted

    Returns:
      None
    '''
    if product_id is not None:
        query = f"DELETE FROM gs.products WHERE product_id = {product_id}"
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


if __name__ == '__main__':

    conn = connect_to_database('postgres', 'postgres',
                               'postgres', 'localhost', '5432')

    if conn:
        get_products(conn)
        insert_product(conn, {'product_name': 'potatoes',
                              'uom_id': '2', 'price_per_unit': '60'})
        delete_product(conn, 11)
        conn.close()
