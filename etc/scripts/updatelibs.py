# This script updates python libraries in the app lib directory if it includes a pip.txt file

import os
import sys
import subprocess

for app in os.listdir('etc/apps'):
    if os.path.isfile(f"etc/apps/{app}/lib/pip.txt"):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "-t", f"etc/apps/{app}/lib", "-r", f"etc/apps/{app}/lib/pip.txt", "--no-dependencies"])