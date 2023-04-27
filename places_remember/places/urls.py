from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'places'
urlpatterns = [
    path('', TemplateView.as_view(template_name='user/login.html')),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/map/', views.map_view, name='map'),
    path('accounts/profile/<int:id>/', views.show_places, name='map_one'),
]
