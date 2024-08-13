from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import razorpay

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def detailspage(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['email'] = request.POST['email']
        request.session['phone'] = request.POST['phone']
        request.session['amount'] = request.POST['amount']
        return redirect('donatepage')
    return render(request, 'detailspage.html')

def donatepage(request):
    if 'amount' in request.session:
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # Amount should be in paisa
        amount = int(request.session['amount']) * 100

        order = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'
        })

        context = {
            'order_id': order['id'],
            'amount': amount,
            'key_id': settings.RAZORPAY_KEY_ID,
            'name': request.session['name'],
            'email': request.session['email'],
            'phone': request.session['phone'],
        }
        return render(request, 'donatepage.html', context)
    return redirect('detailspage')

def successpage(request):
    return HttpResponse("Payment Success")

def failurepage(request):
    return HttpResponse("Payment Failed")