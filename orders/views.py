from django.shortcuts import render, redirect
from .models import Order
from cart.models import Cart
from django.shortcuts import render


def checkout(request):

    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    if request.method == 'POST':

        address = request.POST['address']

        request.session['address'] = address
        request.session['total'] = total

        return redirect('/orders/payment/')

    return render(
        request,
        'orders/checkout.html',
        {'total': total}
    )


def order_history(request):

    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    orders = Order.objects.filter(
        user=request.user
    )

    return render(
        request,
        'orders/history.html',
        {'orders': orders}
    )
def payment(request):

    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    total = request.session.get('total', 0)
    address = request.session.get('address', '')

    cart_items = Cart.objects.filter(user=request.user)

    if request.method == 'POST':
        print("PAY NOW CLICKED")

        Order.objects.create(
            user=request.user,
            address=address,
            total_price=total
        )

        cart_items.delete()

        return render(
            request,
            'orders/success.html'
        )

    return render(
        request,
        'orders/payment.html',
        {'total': total}
    )
