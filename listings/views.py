from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from .forms import ListingForm


# Get all listings
def listings(request):
    listings = Listing.objects.all()
    context = {"listings": listings}
    return render(request, "listings/list.html", context)


# create listing
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
def update_listing(request, id):
    # get listings instance
    listing = get_object_or_404(Listing, id=id, user=request.user)
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("listings")
    else:
        form = ListingForm(instance=listing)
    context = {"form": form}
    return render(request, "listings/edit.html", context)


# delete listing
def delete_listing(request, id):
    listing = get_object_or_404(Listing, id=id, user=request.user)
    if request.method == "POST":
        listing.delete()
        return redirect("listings")
    return render(request, "listings/delete.html", {"listing": listing})
