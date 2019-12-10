import csv

import psycopg2

CREDENTIALS_DB = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'toolsify',
    'user': 'admin',
    'password': 'admin'
}

QUERY = 'SELECT * FROM record'

OUTPUT_CSV_FILE_NAME = 'db_records.csv'

FETCH_ITER_SIZE = 100000


if __name__ == '__main__':
    connection = psycopg2.connect(**CREDENTIALS_DB)
    print(f"Successfully connected to {CREDENTIALS_DB['database']} database...\n")
    cursor = connection.cursor()

    print(f"Executing Query `{QUERY}`...")
    cursor.execute(QUERY)
    print("Query executed!!...\n")

    columns_names = [column.name for column in cursor.description]
    print(f"Columns: {columns_names}\n")

    print(f"Opening {OUTPUT_CSV_FILE_NAME} for copy...")
    with open(OUTPUT_CSV_FILE_NAME, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(columns_names)
        print("Csv file updated with the columns in header...")

        is_fetching_completed = False
        while not is_fetching_completed:
            print("Fetching data...")
            records = cursor.fetchmany(size=FETCH_ITER_SIZE)
            print(f"{len(records)} fetched from database...")
            csv_writer.writerows(records)
            print("Csv file updated...")
            is_fetching_completed = len(records) < FETCH_ITER_SIZE

    print("\nDatabase records successfully imported to csv!!")
    cursor.close()
