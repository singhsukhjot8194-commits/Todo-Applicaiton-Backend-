from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='home'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.user_login, name='login'),
    path('todo/', views.todo, name='todo'),
    path('edit_todo/<int:srno>/', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>/', views.delete_todo, name='delete_todo'),
    path('logout/', views.user_logout, name='logout')
]
