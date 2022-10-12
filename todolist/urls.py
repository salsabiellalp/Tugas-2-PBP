from django.urls import path
from todolist.views import show_todolist, register, login_user 
from todolist.views import logout_user, create_task, delete_task
from todolist.views import change_status, show_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', create_task, name='create_task'),
    path('delete-task/<int:id>', delete_task, name='delete-task'),
    path('change-status/<int:id>', change_status, name='change-status'),
    path('json/', show_json, name='show_json'),
]