import requests
from subprocess import Popen, PIPE
from time import sleep

def warn(per):
    url = "http://ip:9000/send-group-message"
    payload = f'message=%E2%9A%A0%EF%B8%8F%20Server%20VCON%20{per}%25%20%E2%9A%A0%EF%B8%8F&name=ALL'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

def shell(cmd):
    return Popen(cmd, shell=True, stdout=PIPE).stdout.read().decode('utf-8')

temp = 94
while True:
    per = int(shell('df -h --type ext4 | tail -1 | awk \'{print $5}\' | cut -d "%" -f 1'))
    print(per, end='\r')
    if per > 80:
        if per > temp:
            warn(per)
            temp = per
    sleep(60)
