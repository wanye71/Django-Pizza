from django.shortcuts import render

# Create view for home page
def home(request):
    return render(request, 'pizza/home.html')

# Create view for order page
def order(request):
    return render(request, 'pizza/order.html')