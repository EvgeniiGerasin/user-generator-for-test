from django.urls import path
from users_generator import views

app_name = 'users_generator'
urlpatterns = [
    path('', view=views.index, name='index'),
]
