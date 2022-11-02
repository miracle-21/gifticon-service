from django.urls import path

from app.views import *

urlpatterns = [
    path('/product', ProductView.as_view()),
    path('/sale', ProductSaleView.as_view()),
    path('/sale/<int:user_id>', ProductSaleView.as_view()),
    path('/order/<int:product_id>', ProductOrderView.as_view()),
]