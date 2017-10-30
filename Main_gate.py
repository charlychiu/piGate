import requests
import json
import time

lastLine = "" #Init
countLine = 0 #Init

#lastLine = fp.readlines()[-1]   
def init():
    with open('readQr.txt') as fp:
        d=fp.readlines()
        countLine = len(d)

def check_QRcatch():
    with open('readQr.txt') as fp:
        d=fp.readlines()
        tmp = len(d)
        if tmp > countLine:
	    lastLine = fp.readlines()[-1]
            string_handle()
	    network_handle()

def string_handle():
    lastLine = lastLine.strip()
    lastLine = lastLine.split(':')
    lastLine = lastLine[1]
    print lastLine

def network_handle():
    r = requests.post('http://120.105.129.146/api/reqGate', data = {'qrcode_content':lastLine,'action':'in'})
    #res = r.json()
    res = r.text
    j = json.loads(res)
    #print(res)
    print j['result']

init()
while True:
    check_QRcatch()
    time.sleep(5)
