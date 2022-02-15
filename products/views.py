from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    product_list=Product.objects.order_by('name')
    prod_dict={'product_list':product_list}
    return render(request,'products/index.html',context=prod_dict)
def register(request):
    return render(request,'products/register.html')