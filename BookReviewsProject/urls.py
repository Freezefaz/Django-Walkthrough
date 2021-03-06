"""BookReviewsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import books.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books.views.welcome),
    path('books/', books.views.index),
    path('reviews/', reviews.views.index),
    path('publishers/', books.views.show_publisher),
    path('authors/', books.views.show_author),
    path('books/create/', books.views.create_book),
    path('publishers/create', books.views.create_publisher),
    path('authors/create', books.views.create_author),
    path('books/update/<book_id>', books.views.update_book,
         name='update_book_route'),
    path('publishers/update/<publisher_id>', books.views.update_publisher,
         name='update_publisher_route'),
    path('authors/update/<author_id>', books.views.update_author,
         name='update_author_route'),
    path('books/delete/<book_id>', books.views.delete_book,
         name='delete_book_route')
]
