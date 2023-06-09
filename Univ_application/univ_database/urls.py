from django.urls import path, include


from . import views

app_name = 'univ'
urlpatterns = [
    path('', views.admin_home, name='univ_index' ),
    path('prof_roster/', views.prof_index, name='Professor roster'), #F1
        #F2
    path('dept/', views.dept_index, name = 'Department Index'),
    path('dept/<str:dept>',views.dept_overview, name ="Department overview") ,
    path('courses/', views.course_index, name = 'Course Index'), 
    path('perf/', views.prof_perf, name = 'Perfomance Search'), #F3
]

