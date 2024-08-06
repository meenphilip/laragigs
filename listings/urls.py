from django.urls import path
from . import views

urlpatterns = [
    path("", views.listings_list, name="listings-list"),
    path("listing-detail/<int:id>", views.single_listing, name="single-listing"),
]
