from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import filter_and_search_listings
from .models import Listing
from .forms import ListingForm


# Get all listings
def listings(request, tag_slug=None):
    listings, query, tag = filter_and_search_listings(request, tag_slug)
    context = {"listings": listings, "query": query, "tag": tag}
    return render(request, "listings/index.html", context)


# create listing
@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)  # Save form with commit=False
            listing.user = (
                request.user
            )  # Set the current user as the owner of the listing
            listing.save()  # Save the listing instance
            form.save_m2m()  # Save the many-to-many relationships (tags)
            messages.success(request, "Listing created successfully!")
            return redirect("listings")
    else:
        form = ListingForm()
    context = {"form": form}
    return render(request, "listings/create.html", context)


def single_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    # option 2 to get single object
    # listing = Listing.objects.get(id=id)
    context = {"listing": listing}
    return render(request, "listings/show.html", context)


# update listing
@login_required
def update_listing(request, id):
    # get listings instance
    listing = get_object_or_404(Listing, id=id, user=request.user)
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing updated successfully!")
            return redirect("listings")
    else:
        form = ListingForm(instance=listing)
    context = {"form": form}
    return render(request, "listings/edit.html", context)


# delete listing
@login_required
def delete_listing(request, id):
    listing = get_object_or_404(Listing, id=id, user=request.user)
    if request.method == "POST":
        listing.delete()
        messages.success(request, "Listing deleted successfully!")
        return redirect("manage_listings")
    return render(request, "listings/delete.html", {"listing": listing})


# search listings
def search_listings(request):
    listings, query, tag = filter_and_search_listings(request)
    context = {"listings": listings, "query": query, "tag": tag}
    return render(request, "listings/index.html", context)


# Get all listings for the logged-in user
@login_required
def manage_listings(request):
    listings = Listing.objects.filter(user=request.user)
    context = {"listings": listings}
    return render(request, "listings/manage.html", context)
