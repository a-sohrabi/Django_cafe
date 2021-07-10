
from django.shortcuts import render
from django.template import loader

from cafe.models import Orders, MenuItems


# Create your views here.

def order_list(request):
    orders = Orders.objects.all()
    return render(request, 'order_list.html', orders)


def order_detail(request, id):
    context = {}
    context['data'] = Orders.objects.get(id=id)
    return render(request, "order_detail.html", context)
