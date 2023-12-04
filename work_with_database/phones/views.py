from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    context = {}
    phone_obj = Phone.objects.all()
    context['phones'] = phone_obj

    if sort == 'name':
        phone_obj = Phone.objects.order_by('name')
        context['phones'] = phone_obj
    elif sort == 'min_price':
        phone_obj = Phone.objects.order_by('price')
        context['phones'] = phone_obj
    elif sort == 'max_price':
        phone_obj = Phone.objects.order_by('-price')
        context['phones'] = phone_obj

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone_obj = Phone.objects.get(slug=slug)
    context['phone'] = phone_obj
    return render(request, template, context)
