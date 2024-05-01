from django.shortcuts import render
from .forms import PizzaForm

# Create view for home page
def home(request):
    return render(request, 'pizza/home.html')

# Create view for order page
def order(request):
    form = PizzaForm()
    return render(request, 'pizza/order.html', {'pizzaform':form})