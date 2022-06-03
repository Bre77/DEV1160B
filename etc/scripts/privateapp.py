import requests
import sys
import time
from splunkcreds import username, password, authtoken, stack, acs

# Get Splunkbase Auth Token
login = requests.get("https://api.splunk.com/2.0/rest/login/splunk", auth=(username, password))
token = login.json()['data']['token']
app = sys.argv[1]
print(app)

if "/" not in app:
    app = f"/opt/splunk/etc/build/{app}.spl"



upload = requests.post("https://appinspect.splunk.com/v1/app/validate", files={
    'app_package': open(app, 'rb'),
    'included_tags': (None,'private_app')
}, headers={"Authorization": f"Bearer {token}"})
print(upload.json())
rid = upload.json()['request_id']

ready = False
while not ready:
    time.sleep(5)
    check = requests.get(f"https://appinspect.splunk.com/v1/app/validate/status/{rid}", headers={"Authorization": f"Bearer {token}"})
    status = check.json()['status']
    print(status)
    ready = status == "SUCCESS"

result = requests.get(f"https://appinspect.splunk.com/v1/app/report/{rid}", headers={"Authorization": f"Bearer {token}"})
f = open(f"{app}.json", "w")
f.write(result.text)
f.close()

data = result.json()
print(data["summary"])
print("")

if(data["summary"]["failure"] == 0 and data["summary"]["error"] == 0 and data["summary"]["manual_check"] == 0):
    upload = requests.post(f"https://{acs}/{stack}/adminconfig/v2/apps/victoria", data=open(app, 'rb'), headers={
        "X-Splunk-Authorization": token,
        "Authorization": f"Bearer {authtoken}",
        "ACS-Legal-Ack": "Y"
    })
    print(upload.json())
else:
    for report in data['reports']:
        for group in report['groups']:
            for check in group['checks']:
                if check['result'] in ["error","failure","manual_check","warning"]:
                    print(check['messages'])      