from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Store


def home(request):
    context = {
        'stores': Store.objects.all()
    }

    return render(request, 'store/home.html', context)


class StoreListView(ListView):
    model = Store
    template_name = 'store/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'stores'


class StoreDetailView(DetailView):
    model = Store


class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    fields = ['store_name', 'description', 'store_address', 'store_address_2', 'mobile',
              'email', 'city', 'state']
    success_url = '/' # navigate to home page after creating a new store.

    # uncomment when owner is added in models.py
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StoreUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Store
    fields = ['store_name', 'description', 'store_address', 'store_address_2', 'mobile',
              'email', 'city', 'state']
    success_url = '/' # navigate to home page after creating a new store.

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
