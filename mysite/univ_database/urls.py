from django.urls import path, include


from . import views

app_name = 'univ'
urlpatterns = [
    path('', views.univ_index, name='univ_index' )
]

