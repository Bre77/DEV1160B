import requests
import sys
from splunkcreds import username, password

app = sys.argv[1]

try:
    splunkbaseid = open(f"./etc/apps/{app}/.splunkbaseid", "r").read()
except:
    print ("Please create a .splunkbaseid file with the numerical app ID")
    quit()

try:
    package = open(f"./etc/build/{app}.spl", "rb")
except:
    print ("Please package the app first")
    quit()


upload = requests.post(f"https://splunkbase.splunk.com/api/v1/app/{splunkbaseid}/new_release/",
    auth=(username, password),
    files=[("files[]",package)],
    data={
        "splunk_versions": "8.2,8.1,8.0",
        "visibility": "true"
    }
)

print(f"{upload.status_code} {upload.text}")