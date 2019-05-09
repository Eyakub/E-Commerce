from django.db import models
from ecommerce.carts.models import Cart
from ecommerce.utils import unique_order_id_generator
from django.db.models.signals import pre_save
ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    # billing_profile =
    # shipping_address =
    # billing_address =
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    order_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id


def pre_save_create_oder_id(sender, instance, *args, **kwargs):
    if not instance.oder_id:
        instance.oder_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_oder_id, sender=Order)

# generate the order id
# generate the order total?
