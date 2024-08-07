from django.urls import path
from . import views

urlpatterns = [
    path("", views.listings, name="listings"),
    path("listing-detail/<int:id>", views.single_listing, name="single-listing"),
]
