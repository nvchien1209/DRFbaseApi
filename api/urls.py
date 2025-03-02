from django.urls import path
from api import views

urlpatterns = [
    path("",views.Notelist.as_view()),
    path('<int:pk>/',views.NoteDetails.as_view())
]