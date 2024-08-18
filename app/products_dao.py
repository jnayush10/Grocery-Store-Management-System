from sql_connection import connect_to_database


def execute_query(conn, query):
    '''Executes an SQL query and returns the results.
    Args:
      conn: The psycopg2 connection object.
      query: The SQL query to execute.

    Returns:
      A list of tuples containing the query results.
    '''

    with conn.cursor() as cur:
        cur.execute(query)
        results = cur.fetchall()
        return results


if __name__ == '__main__':

    list_of_products = []

    conn = connect_to_database('postgres', 'postgres',
                               'postgres', 'localhost', '5432')

    if conn:
        query = 'SELECT p.product_id, p.name, u.uom_id, u.uom_name, p.price_per_unit FROM gs.products as p inner join gs.uom as u on p.uom_id = u.uom_id ORDER BY product_id ASC'
        products = execute_query(conn, query)
        for (product_id, name, unit_of_measure_id, unit_of_measure, price_per_unit) in products:
            list_of_products.append({
                'product_id': product_id,
                'product_name': name.strip(),
                'uom_id': unit_of_measure_id,
                'uom_name': unit_of_measure.strip(),
                'price_per_unit': price_per_unit
            })
            print(list_of_products)
        conn.close()
