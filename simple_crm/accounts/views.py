from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Product, Order, Customer
from .forms import OrderForm
from .filters import OrderFilter


def home(request):
    orders = Order.objects.all()[0:5]
    customers = Customer.objects.all()

    total_orders = orders.count()
    orders_delivered = Order.objects.filter(status='Delivered').count()
    orders_pending = Order.objects.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending}
    return render(request, 'accounts/dashboard.html', context=context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    orders = customer.order_set.all()
    order_count = orders.count()

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs

    context = {'customer': customer, 'orders': orders, 'count': order_count, 'filter': my_filter}
    return render(request, 'accounts/customers.html', context=context)


def create_order(request, slug):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=6, can_delete=False)
    customer = get_object_or_404(Customer, slug=slug)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context=context)


def update_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context=context)


def delete_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(request, 'accounts/dashboard.html')



