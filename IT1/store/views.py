from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Store
from products.models import Product


def store_detail_view(request, id):
    store = get_object_or_404(Store, id=id)
    context = {
        'store': store,
        'products': Product.objects.all()
    }

    return render(request, 'store/store_detail.html', context)


class StoreListView(ListView):
    model = Store
    template_name = 'store/home.html'  # <app>/<model>_<view_type>.html
    context_object_name = 'stores'


# class StoreDetailView(DetailView):
#     model = Store


class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    fields = ['store_name', 'description', 'store_address', 'store_address_2', 'mobile',
              'email', 'city', 'state', 'country']
    success_url = '/'  # navigate to home page after creating a new store.

    # uncomment when owner is added in models.py
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StoreUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Store
    fields = ['store_name', 'description', 'store_address', 'store_address_2', 'mobile',
              'email', 'city', 'state']
    success_url = '/'  # navigate to home page after creating a new store.

    # uncomment when owner is added in models.py
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # uncomment when owner is added in models.py
    def test_func(self):
        store = self.get_object()
        if self.request.user == store.owner:
            return True
        return False


class StoreDeleteView(LoginRequiredMixin, DeleteView):
    model = Store
    success_url = '/'  # navigate to home page after creating a new store.

    # uncomment when owner is added in models.py
    def test_func(self):
        store = self.get_object()
        if self.request.user == store.owner:
            return True
        return False


# def about(request):
#     return render(request, 'store/about.html')  # {'title': 'About'}

# trial

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "store/store_detail.html", context)


class IndexView(DetailView):
    model = Store

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all()
        return context
