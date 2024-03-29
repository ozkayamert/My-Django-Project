from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html') # Anladığım kadarıyla bu kısım templates kısmını kullanıyor yani templates ile alakalı
# bir bölüm olabilir burası.

def contact(request):
    return render(request, 'core/contact.html')