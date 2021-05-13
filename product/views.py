from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404


def productlist(request, category_slug=None):  # category_slug=None
    category = None
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))
    # paginator = Paginator(productlist, 1)  # Show 1 contacts per page.
    # page = request.GET.get('page')
    # productlist = paginator.get_page(page)

    if category_slug:
        # category = Category.objects.get(category_slug=category_slug)
        category = get_object_or_404(Category, category_slug = category_slug)
        productdetail = productlist.filter(category=category)
 
    search_query = request.GET.get('q')
    if search_query:
        productlist = productlist.filter(
            Q(name__icontains=search_query) |   
            Q(description__icontains=search_query) |
            Q(condition__icontains=search_query) |
            Q(brand__brandName__icontains=search_query) |
            Q(category__categoryName__icontains=search_query)
        )

    paginator = Paginator(productlist, 15)  # Show 15 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'product/product_list.html'
    context = {'product_list': productlist, 'page_obj': page_obj,
               'category_list': categorylist, 'category': category}

    return render(request, template, context)


def productdetail(request, product_slug):
    print(product_slug)
    # productdetail = Product.objects.get(slug=product_slug)
    productdetail = get_object_or_404(Product, slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'product/product_detail.html'
    context = {'product_detail': productdetail, 'product_images': productimages}
    return render(request, template, context)
