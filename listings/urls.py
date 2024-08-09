from django.urls import path
from . import views

urlpatterns = [
    path("", views.listings, name="listings"),
    path("tag/<slug:tag_slug>/", views.listings, name="listings_by_tag"),
    path("listings/create/", views.create_listing, name="create_listing"),
    path("listings/<int:id>/detail/", views.single_listing, name="single-listing"),
    path("listings/<int:id>/edit/", views.update_listing, name="update_listing"),
    path("listings/<int:id>/delete/", views.delete_listing, name="delete_listing"),
    path("listings/manage/", views.manage_listings, name="manage_listings"),
    path("listings/search/", views.search_listings, name="search_listings"),
]

