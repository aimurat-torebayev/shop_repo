from django.urls import path
from myapp.views import index, indexItem

app_name = 'myapp'

urlpatterns = [
    # http://127.0.0.1:8000/myapp/ 
    path('', index),
    path('<int:productId>/', indexItem, name='detail'),
]