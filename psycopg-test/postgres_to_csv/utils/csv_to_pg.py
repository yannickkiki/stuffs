import pandas
import psycopg2

CREDENTIALS_DB = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'csvify',
    'user': 'petitnokoue',
    'password': 'petitnokoue'
}

connection = psycopg2.connect(**CREDENTIALS_DB)
cursor = connection.cursor()
# cursor.execute(query="SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
# records = cursor.fetchall()

# cursor.execute(query="SELECT * FROM record")
# records = cursor.fetchmany(5)

data_csv_file = 'new_data.csv'
columns = pandas.read_csv(data_csv_file, nrows=0).columns.tolist()

#query = "CREATE TABLE IF NOT EXISTS record ("
#for column in columns:
#    query += f"{column} text ,"
#query = query[:-1] + ")"
#cursor.execute(query);
#connection.commit()

with open(data_csv_file, 'r') as file:
    next(file) # to skip the header
    cursor.copy_from(file=file, sep=",", table="record", columns=columns)
connection.commit()
