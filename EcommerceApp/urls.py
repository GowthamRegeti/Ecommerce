from django.urls import path
from EcommerceApp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name="index"),
    path('index.html',views.index,name="index"),
    path('shop.html',views.shop,name="shop"),
    path('blog.html',views.blog,name="blog"),
    path('about.html',views.about,name="about"),
    
    path('contact.html',views.contact,name="contact"),
    #path('login.html',views.login,name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)