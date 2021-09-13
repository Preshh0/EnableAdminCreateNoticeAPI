from django.urls import path
from . import views
# from .views import NoticesCreated

#add url routes here
urlpatterns = [
    path('notice/', views.NoticesCreated, name="NoticesCreated"),
]