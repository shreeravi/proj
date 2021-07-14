from django.contrib import admin
from django.urls import path
from toast import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('del/', views.remove, name="delete"),
    path('admin/', admin.site.urls),
]
