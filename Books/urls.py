from django.urls import path
from Books import views
urlpatterns=[
    path('insert/',views.insertBook),
    path('save/',views.insert),
    path('view/',views.viewBooks),
    path('edit/',views.editBook),
    path('update/',views.edit),
    path('delete/',views.deleteBook),
    path('search/',views.searchBook),
    path('searching/',views.search),
    path('userlogin/',views.userLogin),
    path('userlogout/',views.userLogout),
]