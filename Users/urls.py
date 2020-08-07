from django.urls import path, include

from Users.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]