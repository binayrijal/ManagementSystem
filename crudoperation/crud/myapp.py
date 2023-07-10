import requests
import json
URL="http://127.0.0.1:8000/crudstart/view_student/"

def getdata(id = None):
    data={}

    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

#getdata()

def postdata():
    data={
        'name':'bidu',
        'roll':191512,
        'city':'balkumari',
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
#postdata()

def putdata():
    data={
        'id':3,
        'name':'binu',
        'city':'kharibot'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
putdata()