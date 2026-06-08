from django.shortcuts import redirect, render
from .models import Cart
from products.models import Product


def add_to_cart(request, product_id):

    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    product = Product.objects.get(id=product_id)

    cart_item = Cart.objects.filter(
        user=request.user,
        product=product
    ).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )

    return redirect('/cart')


def remove_from_cart(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()

    return redirect('/cart')


def cart_page(request):

    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return render(
        request,
        'cart/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )
