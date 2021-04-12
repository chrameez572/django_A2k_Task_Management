
from django.contrib import admin
from django.urls import path
from manage_task import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('addandshow' , views.add_show,name="addandshow"),
    path('update<int:id>/', views.update_data, name="update"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('login' , views.login ,name ="login"),
    path('register', views.register, name="register"),

]
