from django.shortcuts import render
from django.views.generic import TemplateView

class Homepage(TemplateView):
     template_name = 'home.html'

class Aboutpage(TemplateView):
     template_name = 'about.html'

class Faqpage(TemplateView):
     template_name = 'FAQ.html'

class Dashboardpage(TemplateView):
     template_name = 'dashboard.html'
     

