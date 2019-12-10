import psycopg2

database_settings = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'pgtest',
    'user': 'yannick',
    'password': 'yannick'
}
# ------------------------------------------------------------------------------------ #
# connection = psycopg2.connect(**database_settings)
#
# cursor1 = connection.cursor()
# cursor1.execute("INSERT INTO employees (first_name) VALUES (%s)", ('Poppy1', ))
# cursor2 = connection.cursor()
# cursor2.execute("INSERT INTO employees (first_name) VALUES (%s)", ('Poppy2', ))
#
# connection.commit()
#
# cursor3 = connection.cursor()
# cursor3.execute("INSERT INTO employees (first_name) VALUES (%s)", ('Poppy3', ))

# ------------------------------------------------------------------------------------ #
# connection1 = psycopg2.connect(**database_settings)
# cursor1 = connection1.cursor()
# cursor1.execute("INSERT INTO employees (first_name) VALUES (%s)", ('CPoppy1', ))
#
# connection2 = psycopg2.connect(**database_settings)
# cursor2 = connection2.cursor()
# cursor2.execute("INSERT INTO employees (first_name) VALUES (%s)", ('CPoppy2', ))
#
# connection1.commit()
# ------------------------------------------------------------------------------------ #
connection = psycopg2.connect(**database_settings)
connection.autocommit = True
cursor = connection.cursor()
cursor.execute("INSERT INTO employees (first_name) VALUES (%s)", ('Velii', ))
