from django.urls import path
from products.views import product_detail_view, product_create_view, dynamic_lookup_view, product_delete_view, product_list_view, search, product_update_view
from .views import add_comment_to_product

appname = 'products'
urlpatterns = [

    #Product - Add, Delete, View, List
    path('products/', product_detail_view),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('create/', product_create_view),
    path('s/', search, name='search'),
    path('', product_list_view, name='product-list'),
    path('<int:id>/comment', add_comment_to_product, name="add_comment_to_product")
]
