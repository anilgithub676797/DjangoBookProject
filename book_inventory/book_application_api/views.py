from django.shortcuts import render
from book_application.models import Book
import json
from django.views.generic import View
from book_application_api.mixins import SerializeMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from book_application_api.utils import is_json
from book_application.forms import BookForm
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class BookCRUDClassBasedView(View,SerializeMixin,HttpResponseMixin):
    def get_book_object_by_id(self,id):
        try:
            book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            book=None
        return book

    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'message': 'Please send valid JSON data'})
            return self.render_to_http_response(json_data, status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            book=self.get_book_object_by_id(id)
            if book is None:
                json_data = json.dumps({'message': 'No matching book found'})
                return self.render_to_http_response(json_data, status=404)
            json_data=self.searilize([book,])
            return self.render_to_http_response(json_data)
        book_query_set = Book.objects.all()
        json_data = self.searilize(book_query_set)
        return self.render_to_http_response(json_data)


    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'message':'Please send valid JSON data'})
            return self.render_to_http_response(json_data,status=400)

        book_data=json.loads(data)
        form = BookForm(book_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'message': 'Book added successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'message': 'Please send valid JSON data'})
            return self.render_to_http_response(json_data, status=400)
        pdata = json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            json_data = json.dumps({'message': 'ID is mandatory to perform updation'})
            return self.render_to_http_response(json_data, status=400)
        book=self.get_book_object_by_id(id)
        if book is None:
                json_data = json.dumps({'message': 'Book not available matching to provided ID'})
                return self.render_to_http_response(json_data, status=404)
        input_data = json.loads(data)
        original_data = {
            'author': book.author,
            'title': book.title,
            'published_date': book.published_date
        }
        original_data.update(input_data)
        form = BookForm(original_data, instance=book)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'message': 'Book updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'message': 'Please send valid JSON data'})
            return self.render_to_http_response(json_data, status=400)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            book=self.get_book_object_by_id(id)
            if book is None:
              json_data = json.dumps({'message': 'Book not available matching to provided ID'})
              return self.render_to_http_response(json_data, status=404)
            status, deleted_item = book.delete()
            if status == 1:
                json_data = json.dumps({'message': 'Book deleted successfully'})
                return self.render_to_http_response(json_data)
            json_data = json.dumps({'message': 'Unable to delete'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'message': 'ID is mandatory to perform deletion'})
        return self.render_to_http_response(json_data, status=400)


