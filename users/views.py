from django.shortcuts import render
from .models import Post,User
# Create your views here.
def index(request):
    users=User.objects.order_by("first_name")
    posts=Post.objects.order_by("user")
    data_list={'users':users,'posts':posts}
    return render(request,'users/index.html',context=data_list)