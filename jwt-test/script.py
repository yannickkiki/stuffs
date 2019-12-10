import jwt

# https://jwt.io/introduction
key = 'secrett'

token = jwt.encode(payload={'some': 'payload'}, key=key, algorithm='HS256')
payload = jwt.decode(jwt=token, key=key, algorithms=['HS256'])


import base64
message = "Python is fun"
message_bytes = message.encode('ascii')
message_encoded_bytes = base64.b64encode(message_bytes)
message_decoded_bytes = base64.b64decode(message_encoded_bytes)
message_decoded = message_bytes.decode('ascii')
