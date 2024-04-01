from django.shortcuts import render

from item.models import Category, Item

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    }) # Anladığım kadarıyla bu kısım templates kısmını kullanıyor yani templates ile alakalı
# bir bölüm olabilir burası.

def contact(request):
    return render(request, 'core/contact.html')