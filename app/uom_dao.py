from sql_connection import connect_to_database


def get_uoms(conn):
    cursor = conn.cursor()
    query = f"SELECT * FROM gs.uom"
    cursor.execute(query)

    response = []
    for row in cursor:
        response.append({
            'uom_id': row[0],
            'uom_name': row[1].strip()
        })
    return response


if __name__ == '__main__':

    connection = connect_to_database('postgres', 'postgres',
                                     'postgres', 'localhost', '5432')

    if connection:
        get_uoms(conn=connection)
        connection.close()
