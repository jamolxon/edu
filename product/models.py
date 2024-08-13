from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.models import BaseUser



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(_("price"), default=100)
    photo = models.ImageField(_("photo"), upload_to="product/%Y/%m")
    is_special = models.BooleanField(_("product is special"), default=False)
    is_accessory = models.BooleanField(_("product is accessory"), default=False)
    is_cloth = models.BooleanField(_("product is a cloth"), default=False)

    class Meta:
        db_table = "product"
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name="carts")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cart"
        verbose_name = _("cart")
        verbose_name_plural = _("carts")

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart {self.cart.id}"

    def total_price(self):
        return f"{self.quantity * self.product.price}"

