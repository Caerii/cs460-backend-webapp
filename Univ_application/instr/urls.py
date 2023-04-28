from django.urls import path, include


from . import views

app_name = 'instr'
urlpatterns = [
    path('', views.instructor_home, name='instructor_home' ),
    path('sections/<str:name>/<int:sem>', views.sections_view, name='sections_view' ),
    path('students/<str:cour>/<str:sec>/<int:sem>/<int:yr>', views.student_view, name='student_view' )
]
