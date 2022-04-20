import requests
import sys
import time
login = requests.get("https://api.splunk.com/2.0/rest/login/splunk", auth=('### SPLUNKBASE USERNAME ###', '### SPLUNKBASE PASSWORD ###'))
token = login.json()['data']['token']
app = sys.argv[1]
print(app)

TAGS = ['cloud','self-service','future']

if "/" not in app:
    app = f"/opt/splunk/etc/build/{app}.spl"

files = {
    'app_package': open(app, 'rb')
}

upload = requests.post("https://appinspect.splunk.com/v1/app/validate", files=files, headers={"Authorization": f"Bearer {token}"})
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

for tag in TAGS:
    print(tag)
    for report in data['reports']:
        for group in report['groups']:
            for check in group['checks']:
                if check['result'] in ["error","failure","manual_check","warning"] and tag in check['tags']:
                    print(check['messages'])
    print("")        