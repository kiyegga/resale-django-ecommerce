from django.shortcuts import render
from .models import Product, ProductImages
from django.core.paginator import Paginator


def productlist(request):
    productlist = Product.objects.all()
    # paginator = Paginator(productlist, 1)  # Show 25 contacts per page.
    # page = request.GET.get('page')
    # productlist = paginator.get_page(page)
    paginator = Paginator(productlist, 1)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'product/product_list.html'
    context = {'product_list': productlist, 'page_obj': page_obj}
    return render(request, template, context)


def productdetail(request, product_slug):
    print(product_slug)
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'product/product_detail.html'
    context = {'product_detail': productdetail, 'product_images': productimages}
    return render(request, template, context)
