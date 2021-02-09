from django.db import models


# Create your models here.
CATEGORY_CHOICES = {
    ('BEVERAGE', 'Beverage'),
    ('FOOD', 'Food'),
    ('ENTERTAINMENT', 'Entertainment')
}


class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=False, blank=True)
    price = models.DecimalField(max_digits=50, decimal_places=2, null=False)

    def __str__(self):
        return f"{self.category}"
