import json

def is_json(data):
    try:
        python_data =  json.loads(data)
        valid=True
    except ValueError:
        valid=False
    return valid