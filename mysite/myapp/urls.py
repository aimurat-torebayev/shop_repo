from django.urls import path
from myapp.views import index, indexItem, add_item, update_item, delete_item

app_name = 'myapp'

urlpatterns = [
    # http://127.0.0.1:8000/myapp/ 
    path('', index, name='index'),
    path('<int:productId>/', indexItem, name='detail'),
    path('additem/', add_item, name='add_item'),
    path('updateItem/<int:productId>/', update_item, name='update_item'),
    path('deleteItem/<int:productId>/', delete_item, name='delete_item'),
]