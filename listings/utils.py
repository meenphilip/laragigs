from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Listing
from taggit.models import Tag
from django.shortcuts import get_object_or_404


def filter_and_search_listings(request, tag_slug=None):
    query = request.GET.get("q", "")
    listings = Listing.objects.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        listings = listings.filter(tags__in=[tag])

    if query:
        listings = listings.filter(
            Q(company_name__icontains=query)
            | Q(job_title__icontains=query)
            | Q(location__icontains=query)
            | Q(description__icontains=query)
            | Q(tags__name__icontains=query)
        ).distinct()

    return listings, query, tag


def paginate_listings(request, listings, results_per_page=4):
    # Paginate by 2 per page
    paginator = Paginator(listings, results_per_page)
    # get current page number
    page_number = request.GET.get("page")
    try:
        listings = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        listings = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        listings = paginator.page(paginator.num_pages)

    return listings
