from django.db import models


# Create your models here.
GENDER_CHOICES = (
    ('MASCULINO', 'masculino'),
    ('FEMININO', 'feminino'),
    ('OUTROS', 'outros')
)


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    doc_number = models.CharField(max_length=14, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False, blank=True)

    def __str__(self):
        return f"{self.gender}"
