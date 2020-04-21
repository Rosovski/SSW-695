
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product
from django.db.models import Q
from store.models import Store
from django.contrib.auth.models import User
from django.views.generic import ListView

# Create your views here.

# Check if Product Exist


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


# To Delete a Product
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)


# To Create a Product
def product_create_view(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product_instance = form.save(commit=False)
        stores = Store.objects.all()
        for store in stores:
            if store.owner_id == request.user.id:
                product_instance.store_name = store.store_name
                product_instance.store = store
                product_instance.save()
                form = ProductForm()

    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)


# edit view
def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


# View Product on Product Page
def product_detail_view(request):
    obj = Product.objects.get(id=5)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


# List of all the Products
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


# Search Field - Products
def search(request):
    try:
        q = request.GET.get("q")
    except:
        q = None
    if q:
        queryset = Product.objects.filter(title__icontains=q)
        context = {'query': q, 'products': queryset}
        template = 'products/results.html'
    else:
        template = 'products/home.html'
        context = {}
    return render(request, template, context)



# trial
# class IndexView(ListView):
#     context_object_name = 'prod_list'
#     template_name = 'store/store_detail.html'
#     queryset = Product.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['name'] = Product.objects.all()
#         context['owner_id'] = User.objects.all()
#         return context
