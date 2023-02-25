from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.all_books),
    path('<int:book_id>/', views.one_book),
    path('create/', views.CreateBook.as_view()),
    path('delete/<int:pk>/', views.DeleteBook.as_view()),
    path('update/<int:pk>/', views.UpdateBook.as_view()),

]
