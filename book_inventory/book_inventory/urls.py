"""book_inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from book_application.views import retrieve_books_view,create_book_view,delete_book_view,update_book_view
from book_application_api.views import BookCRUDClassBasedView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',retrieve_books_view),
    re_path(r'^create$',create_book_view),
    re_path(r'^delete/(?P<id>\d+)/$',delete_book_view),
    re_path(r'^update/(?P<id>\d+)/$',update_book_view),
    # re_path(r'^api/(?P<id>\d+)/$',BookDetailsClassBasedView.as_view()),
    re_path(r'^api/$',BookCRUDClassBasedView.as_view()),

]
