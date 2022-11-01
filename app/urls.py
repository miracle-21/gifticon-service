from django.urls import path

from app.views import *

urlpatterns = [
    path('/product', ProductView.as_view()),
    path('', ProductUserView.as_view()),
    path('/<int:user_id>', ProductUserView.as_view()),
]