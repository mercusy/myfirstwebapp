from django.urls import path
from .views import Homepage as home
from .views import Aboutpage as about
from .views import Dashboardpage as dash
from .views import Faqpage as faq

urlpatterns = [
     path('', home.as_view(), name = 'home'),
     path('about/', about.as_view(), name = 'about'),
     path('dashboard/', dash.as_view(), name = 'dashboard'),
     path('faq/', faq.as_view(), name = 'FAQ'),
]