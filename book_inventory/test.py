import json
import requests

BASE_URL="http://127.0.0.1:8000/"
ENDPOINT="api/"

def get_resource(id=None):
    data={}
    if id is not None:
        data={
            'id':id
        }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

#get_resource()
#get_resource()

def create_resource():
    new_book={
        'author':'John Hasting',
        'title':'Life',
        'published_date':'2020-10-25'

    }
    response=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_book))
    print(response.status_code)
    print(response.json())

#create_resource()


def update_resource(id):
    new_book = {
        'id': id,
        'author': 'Nick',
        'title': 'Python',
        'published_date': '2020-10-25'

    }
    response = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_book))
    print(response.status_code)
    print(response.json())

#update_resource(18)

def delete_resource(id):
    book={
        'id': id
    }
    response = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(book))
    print(response.status_code)
    print(response.json())

delete_resource(12)