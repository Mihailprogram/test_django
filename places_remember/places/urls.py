from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'places'
urlpatterns = [
    path('', TemplateView.as_view(template_name='user/login.html')),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/map/', views.map_view, name='map'),
]
