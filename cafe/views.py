from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView

from .models import *


# Create your views here.

# def order_list(request):
#     orders = get_list_or_404(Orders)
#     return render(request, 'order_list.html', {'orders': orders})
#
#
# def order_detail(request, id):
#     context = {'data': Orders.objects.get(id=id)}
#     return render(request, "order_detail.html", context)

# class OrderListView(ListView):
#
#     template_name = 'order_list.html'
#
#     model = Orders
#
#     def get(self, *args, **kwargs):
#         context = super().get(*args, **kwargs)
#
#         return context
#
#
# class OrderDetailView(DetailView):
#     template_name = 'order_detail.html'
#     model = Orders
#
#     def get(self, *args, **kwargs):
#         context = super(OrderDetailView,self).get(*args, **kwargs)
#         return context


def home(request):
    home_ = User.objects.all()
    return render(request, 'home.html', {'home': home_})


def about_us(request):
    about_ = User.objects.all()
    return render(request, 'about_us.html',  {'about_us': about_})


def contact(request):
    contact_ = User.objects.all()
    return render(request, 'contact.html',  {'contact': contact_})


def menu_list(request):
    menu_list_ = User.objects.all()
    return render(request, 'menu_list.html', {'menu_list': menu_list_})


