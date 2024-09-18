from django.urls import path
from .views import BookFormView, FormSuccessView, BookDetailView, BookCreateView, BookListView, \
    BookUpdateView, BookDeleteeView, DeleteSucessView  # Correction ici
urlpatterns=[
    path('book_form/', BookFormView.as_view(), name='book_form'),
    path('form_success/', FormSuccessView.as_view(), name='form_success'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book_update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>', BookDeleteeView.as_view(), name='book_delete'),
    path('delete_success/', DeleteSucessView.as_view(), name='delete_success'),

]
