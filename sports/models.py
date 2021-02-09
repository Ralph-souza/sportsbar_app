from django.db import models


# Create your models here.
MODALITIES_CHOICE = {
    ('FOOTBALL', 'Football'),
    ('SOCCER', 'Soccer'),
    ('VOLLEY', 'Volley'),
    ('RACES', 'Races'),
    ('FIGHT', 'Fight')
}


class Sports(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    modality = models.CharField(max_length=100, choices=MODALITIES_CHOICE, null=False, blank=True)
    bet_value = models.DecimalField(max_digits=50, decimal_places=2, null=False)

    def __str__(self):
        return f"{self.modality}"
