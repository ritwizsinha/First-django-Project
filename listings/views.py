from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator

def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published = True)
    paginator = Paginator(listings,6)
    page  = request.GET.get('page')
    listings_page = paginator.get_page(page)
    context = {
        'listings' : listings_page
    }
    return render(request, 'listings/listings.html', context)


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
