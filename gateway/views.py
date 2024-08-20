from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return render(request,'gateway/main.html')

def payment(request):
    context = {
        'paypal_url': 'https://www.sandbox.paypal.com/invoice/s/create',
        'creditcard_url': '',
    }
    return render(request,'gateway/payment.html',context)