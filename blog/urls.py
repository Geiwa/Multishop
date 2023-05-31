from django.urls import path
from .views import *

urlpatterns = [
  path('',ProductCategoryView.as_view(), name = 'index'),
  path('contact/', contact, name='contact'),
  path('checkout/', checkout, name='checkout'),
  path('detail/', detail,name='detail'),
  path('shop/', ShopListView.as_view(), name='shop'),
  path('detail/<slug:slug>/', ShopDetail.as_view(), name='detail'),

]