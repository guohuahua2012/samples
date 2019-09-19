# -*-coding: utf-8 -*-

import json
import requests

URL = 'https://api.github.com'

def build_url(endpoint):
    res_url = '/'.join([URL, endpoint])
    return res_url

def better_print(json_str):
    res_print = json.dumps(json.loads(json_str), indent=4)
    return res_print

def request_method():
    response = requests.get(build_url('users/caolanmiao'))
    response_text = response.text
    return better_print(response_text)



res = request_method()
print(res)