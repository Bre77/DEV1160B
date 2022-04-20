# Get Config Explorer
Download [**Config Explorer**](https://splunkbase.splunk.com/app/4353/) by [Chris Younger](https://github.com/ChrisYounger).

# DEV1160B
This repository contains the configuration and scripts presented at Splunk .conf22.

You can register for this talk at https://conf.splunk.com/sessions.html?search=DEV1160B

## Scripts

### package.sh
This script requires BASH 4.0 or newer, as it uses the **globstar** option.
You can check you have globstar by running `shopt | grep globstar`
### appinspect.py
This file requires you to hard code your Splunkbase (splunk.com) credentials on line 4.
> auth=('### SPLUNKBASE USERNAME ###', '### SPLUNKBASE PASSWORD ###')