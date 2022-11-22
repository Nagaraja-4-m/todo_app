from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index_page'),
    path('dashboard',views.dashboard, name='user_dashboard'),
    path('add-task',views.addTask, name='add_new_task'),
    path('delete-task/<int:id>',views.deleteTask, name='delete_task'),
    path('complete-task/<int:id>',views.completedTask, name='complete_task'),
]
