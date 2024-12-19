from django.urls import path

from .views import book_event, create_coupon, manage_coupon, add_event





urlpatterns = [

  path('book/', book_event, name='book_event'),

  path('api/create-coupon/', create_coupon, name='create_coupon'),
  path('api/coupon/', manage_coupon, name='list_coupons'),
  path('api/coupon/<str:code>/', manage_coupon, name='manage_coupon'),
  path('add-event/', add_event, name='add_event'),

]



