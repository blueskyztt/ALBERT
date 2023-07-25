# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

url = "http://localhost:8080/predictions/albert"
data = "Hello I'm a [MASK] dog."

data = json.dumps(data)
res = requests.post(url=url, data=data)
if res.ok:
    res = res.text
    res = json.loads(res)
    print(res)
else:
    print("error....")
