import splunklib.client as client

HOST = "localhost"
PORT = 8089
USERNAME = "jntorres217"
PASSWORD = "Jaconian@1520"

# Create a Service instance and log in 
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Print installed apps to the console to verify login
for app in service.apps:
    print (app.name)

# Create a oneshot input

# Retrieve the index for the data
myindex = service.indexes["test_index"]

# Create a variable with the path and filename
uploadme = r"C:\Users\jaket\PythonTesting\practice.txt"

# Upload and index the file
myindex.upload(uploadme);

print (myindex)

# Get the collection of indexes
indexes = service.indexes

# List the indexes and their event counts
for index in indexes:
    count = index["totalEventCount"]
    print ("%s (events: %s)" % (index.name, count))