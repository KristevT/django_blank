from django.db import models
from django.core.exceptions import ValidationError
from uuid import uuid4
from datetime import datetime, date


def check_positive(value):
    if value < 0:
        raise ValidationError(f'Value [{value}] must be positive')

def check_date(datetime_: datetime):
    if datetime_ > datetime.now:
        raise ValidationError('Cannot be created in the future')


class CreatedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        check_date(self.created)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class Category(UUIDMixin, CreatedMixin):
    title = models.TextField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)

    @property
    def max_price(self) -> float:
        return max([product.price for product in self.product_set.all()], default=0)
    
    @property
    def min_price(self) -> float:
        return min([product.price for product in self.product_set.all()], default=0)

    def __str__(self) -> str:
        return self.title


class Product(UUIDMixin, CreatedMixin):
    title = models.TextField(max_length=30, blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[check_positive])

    def save(self, *args, **kwargs):
        check_positive(self.price)
        super().save(*args, **kwargs)

    description = models.TextField(max_length=500, blank=True, null=True)
    expiration_date = models.DateField()
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    @property
    def is_fine(self) -> bool:
        if self.expiration_date is None:
            return True
        return self.expiration_date > date.today()

    def __str__(self) -> str:
        return self.title