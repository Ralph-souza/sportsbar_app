from django.db import models


# Create your models here.
TEAM_MODALITY = {
    ('FOOTBALL', 'Football'),
    ('SOCCER', 'Soccer'),
    ('VOLLEY', 'Volley'),
    ('RACES', 'Races'),
    ('FIGHT', 'Fight')
}


class Team(models.Model):
    team_name = models.CharField(max_length=100, null=False, blank=False)
    team_modality = models.CharField(max_length=100, choices=TEAM_MODALITY, null=False)

    def __str__(self):
        return f"{self.team_modality}"
