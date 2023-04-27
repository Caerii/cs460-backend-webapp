from django.urls import path, include


from . import views

app_name = 'stud'
urlpatterns = [
    path('', views.student_home, name='stud_index' ),
    path('sections/<str:dept>/<int:sem>/<int:yr>', views.course_view, name='course_view' )
]

