# Get Config Explorer
Download [**Config Explorer**](https://splunkbase.splunk.com/app/4353/) by [Chris Younger](https://github.com/ChrisYounger).

# DEV1160B
This repository contains the configuration and scripts presented at Splunk .conf22.

You watch the presentation at [.conf Online - DEV1160B](https://conf.splunk.com/watch/conf-online.html?search=DEV1160B&search.event=conf22&locale=watch#/) or directly [here](https://conf.splunk.com/files/2022/recordings/DEV1160B_1080.mp4).

## Scripts

### package.sh
This script requires BASH 4.0 or newer, as it uses the **globstar** option.
You can check you have globstar by running `shopt | grep globstar`

### appinspect.py
This script requires your Splunkbase (splunk.com) credentials be added to splunkcreds.py

### privateapp.py
This script requires your Splunkbase (splunk.com) credentials, and the Splunk stack with auth token be added to splunkcreds.py

### upload.py
This script requires your Splunkbase (splunk.com) credentials be added to splunkcreds.py, and for the app to include a .splunkbase file that has the numerical app ID.

### updatelibs.py
This script uses the pip.txt file inside an app's lib/ directory to handle python dependencies updates in bulk.

## config_explorer.conf
All the hooks are defined in /etc/apps/DEV1160B/local/config_explorer.conf, which you can either copy into your Config Explorer settings, or install as a seperate app.

## .gitignore
The example .gitignore file can be found at etc/apps/DEV1160B/.gitignore, and should be in the same directory as your .git repo.
