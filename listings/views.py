from django.shortcuts import render, get_object_or_404
from .models import Listing


# Get all listings
def listings_list(request):
    listings = Listing.objects.all()
    context = {"listings": listings}
    return render(request, "listings/listings_list.html", context)


def single_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    context = {"listing": listing}
    return render(request, "listings/listing_details.html", context)
