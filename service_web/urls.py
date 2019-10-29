from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('callback/', views.LoginCallbackView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('test/', views.TestView.as_view()),
]

