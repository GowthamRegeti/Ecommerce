from django.shortcuts import render,redirect
from .models import FeatureProducts,ProProducts
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.encoding import DjangoUnicodeDecodeError
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.urls import NoReverseMatch,reverse
from django.core.mail import EmailMessage
# Create your views here.
def index(request):
    context = FeatureProducts.objects.all()
    proproducts = ProProducts.objects.all()
    return render(request,'index.html',{'context':context,'proproducts':proproducts})

def shop(request):
    return render(request,'shop.html')
def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')




