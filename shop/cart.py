from decimal import Decimal
from django.conf import settings
from shop.models import Tea

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, tea, quantity=1, update_quantity=False):
        tea_id = str(tea.id)
        if tea_id not in self.cart:
            self.cart[tea_id] = {'quantity': 0, 'price': str(tea.price)}
        if update_quantity:
            self.cart[tea_id]['quantity'] = quantity
        else:
            self.cart[tea_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, tea):
        tea_id = str(tea.id)
        if tea_id in self.cart:
            del self.cart[tea_id]
            self.save()

    def __iter__(self):
        tea_ids = self.cart.keys()
        teas = Tea.objects.filter(id__in=tea_ids)
        for tea in teas:
            self.cart[str(tea.id)]['tea'] = tea
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.save()
