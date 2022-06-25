import json

import requests

BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE + "/zlecenie/210212001")
print(response.json())
response = requests.post(BASE + "/zlecenie/210212005",json.dumps({"zlec_klient": "Karol_tengri","zlec_uslug": "Nap-Dor"}))
print(response.json())