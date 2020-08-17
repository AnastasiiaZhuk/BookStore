from django.urls import path

from Orders.views import OrderPageView, charge

urlpatterns = [

    path('charges/', charge, name='charge'),
    path('', OrderPageView.as_view(), name='orders'),
]