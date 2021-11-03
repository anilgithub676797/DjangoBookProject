from django.core.serializers import serialize
from django.http import HttpResponse
import json

class SerializeMixin(object):

    def searilize(self,querySet):
        json_data = serialize('json',querySet)
        python_books_data = json.loads(json_data)
        final_list=[]
        for object in python_books_data:
            book_data=object['fields']
            final_list.append(book_data)
        json_data=json.dumps(final_list)
        return json_data

class HttpResponseMixin(object):
    def render_to_http_response(self,json_data,status=200):
        return  HttpResponse(json_data,content_type='application/json',status=status)

