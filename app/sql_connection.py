import psycopg2

__cnx = None


def connect_to_database(dbname, user, password, host, port):
    '''Connects to a PostgreSQL database and returns a connection object.
    Args:
      dbname: The name of the database.
      user: The username for the database.
      password: The password for the user.
      host: The hostname of the database server.
      port: The port number of the database server.

    Returns:
      A psycopg2 connection object.
    '''
    global __cnx

    if __cnx is None:
        try:
            __cnx = psycopg2.connect(
                database=dbname, user=user, password=password, host=host, port=port)
        except psycopg2.Error as e:
            print(f"Error connecting to database: {e}")
    return __cnx
