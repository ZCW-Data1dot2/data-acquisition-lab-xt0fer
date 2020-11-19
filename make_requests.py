#!/usr/bin/env python3

# NOAA locations data acq lab.
import requests as rq
import os
import json

def test_x():
# Make a connection pool.

# Make a request.
    r = rq.request('get', 'https://httpbin.org/ip')

# View response data.
    print(r.json())
# {'ip': '172.69.48.124'}

# test_x()

def saveJson(seq_num, jsondata):
    if jsondata == None:
        print("No Json Data")
        return
    filename = "./dataNOAA_locations_"+str(seq_num)+".json"
    with open(filename, 'w') as json_file:
        json.dump(jsondata, json_file)


def call_NOAA():
    u = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?offset={offset}&limit={limit}"
    limit = 1000
    offset = 1
    ctype = "application/json"
    key = "NOAA_TOKEN"
    token = os.getenv(key)
    headers = {'Content-Type': ctype,
    'token': token,
    }

    for i in range(1, 39000, 1000):
        offset = i
        set_num = offset // 1000
        url = f"https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?offset={offset}&limit={limit}"
        print("url", url)
        r = rq.get(url, headers=headers)
        if r.status_code != 200:
            print("error in fetching", r.status_code, r.reason)
            return
        saveJson(set_num, r.json())


call_NOAA()