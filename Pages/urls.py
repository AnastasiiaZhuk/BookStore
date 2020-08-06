from django.urls import path
from Pages.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]