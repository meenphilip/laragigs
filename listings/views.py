from django.shortcuts import render, get_object_or_404, redirect
from .utils import filter_and_search_listings, paginate_listings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from .models import Listing
from .forms import ListingForm


# Get all listings
def listings(request, tag_slug=None):
    listings, query, tag = filter_and_search_listings(request, tag_slug)
    listings = paginate_listings(request, listings)
    context = {
        "listings": listings,
        "query": query,
        "tag": tag,
        "search_url": reverse("search_listings"),  # Set the action URL for search
    }
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


# Search in listings (for the index page)
def search_listings(request):
    listings, query, tag = filter_and_search_listings(request)
    listings = paginate_listings(request, listings)
    context = {"listings": listings, "query": query, "tag": tag}
    return render(request, "listings/index.html", context)


# Get all listings for the logged-in user
@login_required
def manage_listings(request):
    listings = Listing.objects.filter(user=request.user)
    listings = paginate_listings(request, listings)
    context = {
        "listings": listings,
        "search_url": reverse(
            "search_manage_listings"
        ),  # Set the action URL for manage search
    }
    return render(request, "listings/manage.html", context)


# Search in manage listings (for the manage page)
@login_required
def search_manage_listings(request):
    query = request.GET.get("q", "")
    listings = Listing.objects.filter(
        Q(user=request.user)
        & (Q(job_title__icontains=query) | Q(company_name__icontains=query))
    )
    listings = paginate_listings(request, listings)
    context = {"listings": listings, "query": query}
    return render(request, "listings/manage.html", context)
