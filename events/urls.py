from django.urls import path
from events import views

urlpatterns = [
    path('events/', views.event_list),
    path('events/<int:pk>/', views.event_detail),
]

