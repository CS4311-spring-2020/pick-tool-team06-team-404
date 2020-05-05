import os

import splunklib.client as client
import splunklib.results as results


class Logentry(object):

    def __init__(self, identifier, timestamp, content, host, source, source_type):
        self.timestamp = timestamp
        self.identifier = identifier
        self.content = content
        self.host = host
        self.source = source
        self.source_type = source_type


HOST = "localhost"
PORT = 8089
USERNAME = "admin"
PASSWORD = "changeme"


class Splunkimport:
    def __init__(self):
        self.service = client.connect(
            host=HOST,
            port=PORT,
            username=USERNAME,
            password=PASSWORD)

    def upload_logfiles(self, directory_path):
        print("Uploading directory ", directory_path)
        for root, dirs, files, in os.walk(directory_path):
            for name in files:
                path = os.path.join(root, name)
                self.upload_logfile(path)
        return 0

    def upload_logfile(self, file_path):
        print('Uploading ', file_path)
        index = self.service.indexes["test_index"]
        index.upload(file_path)

    def transform_to_logentry(self, result):
        return Logentry(identifier=result['_bkt'], timestamp=result['_time'], content=result['_raw'],
                        host=result['host'], source=result['source'], source_type=result['sourcetype'])

    def retrieving_splunk_events(self):
        jobs = self.service.jobs
        entries = list()
        kwargs_blockingsearch = {"exec_mode": "blocking"}
        searchquery_blocking = "search * | head 100"
        job = jobs.create(searchquery_blocking, **kwargs_blockingsearch)
        for result in results.ResultsReader(job.results()):
            print(result)
            entries.append(self.transform_to_logentry(result))
        return entries

    def transform_log_entry(self):
        # status = await self.upload_logfiles(log_file_directory_path)
        entries = self.retrieving_splunk_events()

        for entry in entries:
            print("host: " + entry.host + "\ncontent: " + entry.content + "\nsource: " + entry.source + "\ntime: "
                  + entry.timestamp)
            print("===========")
        return entries

# Print installed apps to the console to verify login
# for app in service.apps:
#    print (app.name)

# Retrieve the index for the data
# myindex = service.indexes["test_index"]

# Create a variable with the path and filename
# filePath = r"C:\Users\jaket\PythonTesting\practice.txt"

# Upload and index the file
# myindex.upload(filePath)

# print (myindex)
