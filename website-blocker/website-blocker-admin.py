import ctypes
import sys

import time
from datetime import datetime as dt


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    print(is_admin())
    # Code of your program here
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    host_temp = r'hosts'
    redirect = "127.0.0.1"
    website_list = ["www.facebook.com", "facebook.com",
                    "www.youtube.com", "youtube.com"]

    while True:
        if(dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16)):
            with open(host_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write("127.0.0.1 "+website+"\n")
        else:
            with open(host_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
        time.sleep(5)
else:
    # Re-run the program with admin rights
    print('asdsad')
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
