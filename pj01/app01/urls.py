


from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'index.html', views.index4),
    url(r'register', views.register, name="reg"),
]