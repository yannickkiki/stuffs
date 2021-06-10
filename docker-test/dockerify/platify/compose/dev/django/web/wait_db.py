import socket
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

db_host, db_port = os.environ['POSTGRES_HOST'], os.environ['POSTGRES_PORT']
while True:
    try:
        s.connect((db_host, int(db_port)))
        s.close()
        break
    except socket.error:
        time.sleep(0.1)
