from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import bedroom_choices,price_choices,state_choices


def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published = True)
    paginator = Paginator(listings,6)
    page  = request.GET.get('page')
    listings_page = paginator.get_page(page)
    context = {
        'listings' : listings_page
    }
    return render(request, 'listings/listings.html', context)


def listing(request,listing_id):

    listing = get_object_or_404(Listing,pk = listing_id)

    content = {
     'listing' : listing,
     
    }

    return render(request, 'listings/listing.html',content)


def search(request):
    query_listings = Listing.objects.all().order_by('-list_date').filter(is_published = True)

    #Keyword
    if 'keywords' in request.GET:
        keyword = request.GET['keywords']
        if keyword :
            query_listings = query_listings.filter(description__icontains = keyword)

    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city :
            query_listings = query_listings.filter(city__iexact = city)

    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state :
            query_listings = query_listings.filter(state__iexact = state)
    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms :
            query_listings = query_listings.filter(bedrooms__lte = bedrooms)

    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price :
            query_listings = query_listings.filter(bedrooms__lte = price)



    content = {
        'listings': query_listings,
        'state_choices':state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices' : price_choices,
        'values': request.GET
    }

    return render(request, 'listings/search.html',content)
