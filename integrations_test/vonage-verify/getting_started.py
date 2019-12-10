import nexmo

client = nexmo.Client(key=None, secret=None)

# Make a request
response = client.start_verification(number="22962718992", brand="Almeki", code_length="4")
print(response)
if response["status"] == "0":
    print("Started verification request_id is %s" % (response["request_id"]))
else:
    print("Error: %s" % response["error_text"])

# Check a request
request_id = response['request_id']
response = client.check_verification(request_id='10eb26d9eddf422f82d841012b11df8f', code="0728")
if response["status"] == "0":
    print("Verification successful, event_id is %s" % (response["event_id"]))
else:
    print("Error: %s" % response["error_text"])


# # Cancel a request
# response = client.cancel_verification(request_id='xxx')
# if response["status"] == "0":
#     print("Cancellation successful")
# else:
#     print("Error: %s" % response["error_text"])
