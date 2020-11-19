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
    filename = "./dataNOAA_locations"+seq_num+".json"
    with open(filename, 'w') as json_file:
        json.dump(jsondata, json_file)


def call_NOAA():
    u = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?offset=XX&limit=XX"
    limit = 1000
    offset = 1
    ctype = "application/json"
    key = "NOAA_TOKEN"
    token = os.getenv(key)
    headers = {'Content-Type': ctype,
    'token': token,
    }
    #print(token)
    r = rq.get(u, headers=headers)
    #if r.status_code != "200":
    print(r.status_code, r.reason)
    print(r.json())


call_NOAA()