from django.urls import path

from . import views

app_name = 'page'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]