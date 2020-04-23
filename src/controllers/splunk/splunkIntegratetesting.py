from src.controllers.splunk import SplunkTest

DIRECTORY_PATH = r"C:\Users\eddyt\PycharmProjects\pick\res\splunk"

print("BEGIN")
testing = SplunkTest.Splunkimport()
testing.upload_logfiles(DIRECTORY_PATH)
testing.transform_log_entry()
print("END")