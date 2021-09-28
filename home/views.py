from django.shortcuts import render, HttpResponse, redirect
from home.models import Order, Update
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def trackorder(request):
    return render(request, 'trackorder.html')

def search(request):
    if request.method=='POST':
        orderId = request.POST.get('orderId')
        allOrders = Order.objects.filter(order_id=orderId)
        allUpdates = Update.objects.filter(order_id=orderId)
        params = {'allOrders': allOrders, 'allUpdates': allUpdates, 'orderId': orderId}
        return render(request, 'searchorder.html', params)
    else:
        return redirect('trackorder.html')