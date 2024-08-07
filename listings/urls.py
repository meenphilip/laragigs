from django.urls import path
from . import views

urlpatterns = [
    path("", views.listings, name="listings"),
    path("create_listings/", views.create_listing, name="create"),
    path("listing-detail/<int:id>/", views.single_listing, name="single-listing"),
    path("listing-update/<int:id>/", views.update_listing, name="listing_update"),
    path("listing-delete/<int:id>/", views.delete_listing, name="delete"),
]
