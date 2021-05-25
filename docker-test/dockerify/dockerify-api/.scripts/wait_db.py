import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

db_host, db_port = 'postgresdb', 5432
# db_host, db_port = "127.0.0.1", 5432
while True:
    try:
        s.connect((db_host, db_port))
        s.close()
        break
    except socket.error:
        time.sleep(0.1)
