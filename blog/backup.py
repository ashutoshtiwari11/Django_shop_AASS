from django.shortcuts import render
from django.http import HttpResponse
from .models import Product as pr
import math
# Create your views here.


def shop(request):
    # querry = list(pr.objects.values_list('cat', flat=True).distinct())
    # list_cat = list(querry)
    # categorywise={}
    # for cate in list_cat:
    #     products = list(pr.objects.filter(cat = cate))
    #     categorywise[cate] = (products)
       from itertools import groupby
       from operator import attrgetter
       from .models import Product
       
       # Step 1: Fetch the products from the database
       products = Product.objects.all().order_by('cat', 'name')
       
       # Step 2: Categorize the products using itertools.groupby
       categorized_products = {} #groupby groups items in a list of memory sequest which is location of memory
       for category, products_in_category in groupby(products, key=attrgetter('cat')):
           categorized_products[category] = list(products_in_category)
       #main problem in this type of code is the querry list 
       # Step 3: Print the categorized products
       print(categorized_products)
       for category, products in categorized_products.items():
           print(f"Category: {category}")
           products_copy = list(products)  # Create a copy of the iterator
           for product in products_copy:
               print(f"- {product.name}")
       
       return render(request,"blog/index.html", { 'product': pr, 'categorized_products': categorized_products})

    

def about(request):
    return render(request, '../templates/blog/about.html')

# def blog(request):
#     return render(request, '../templates/blog/index.html')

# def blog(request):
#     return render(request, '../templates/blog/index.html')