from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_students, name='list_students'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
]

