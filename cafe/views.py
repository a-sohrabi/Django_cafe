from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from cafe.models import Orders, MenuItems


# Create your views here.

def order_list(request):
    orders = Orders.objects.all()
    template = loader.get_template('order_list.html')
    context = {'orders': orders}
    return HttpResponse(template.render(context, request))


def order_detail(request):
    order = Orders.objects.get(id=Orders.number)
    return render()
