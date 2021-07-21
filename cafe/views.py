from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView

from cafe.models import Orders, MenuItems


# Create your views here.

# def order_list(request):
#     orders = get_list_or_404(Orders)
#     return render(request, 'order_list.html', {'orders': orders})
#
#
# def order_detail(request, id):
#     context = {'data': Orders.objects.get(id=id)}
#     return render(request, "order_detail.html", context)

class OrderListView(ListView):

    template_name = 'order_list.html'

    model = Orders

    def get(self, *args, **kwargs):
        context = super().get(*args, **kwargs)

        return context


class OrderDetailView(DetailView):
    template_name = 'order_detail.html'
    model = Orders

    def get(self, *args, **kwargs):
        context = super(OrderDetailView,self).get(*args, **kwargs)
        return context


def home(request):
    return render(request, 'home.html')
