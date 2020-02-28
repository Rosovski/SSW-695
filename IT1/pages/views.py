from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "this_is_true": True,
        "my_number": "202342141224",
        "my_list": [123, 312, 65, "ABC"]
    }
    return render(request, 'about.html', my_context)


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


"""
def contact_view(request, *args, **kwargs):
    return HttpResponse('<h2>Contact View</h2>')
    """
