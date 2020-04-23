from django.urls import path
from .views import (
    StoreListView,
    # StoreDetailView,
    StoreCreateView,
    StoreUpdateView,
    StoreDeleteView,
    store_detail_view
)


urlpatterns = [

    path('store/', StoreListView.as_view(), name='store-home'),
    path('store/<int:id>/', store_detail_view, name='store-detail'),
    # path('store/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
    path('store/register/', StoreCreateView.as_view(), name='store-register'),
    path('store/<int:pk>/update/', StoreUpdateView.as_view(), name='store-update'),
    path('store/<int:pk>/delete/', StoreDeleteView.as_view(), name='store-delete'),
]
