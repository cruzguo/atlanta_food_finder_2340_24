#created in the polls folder manually
from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("detail/", views.rest_info,name="detail view")
]