from django.db import models

# Create your models here.


class Game(models.Model):
    player_name = models.CharField(max_length=255)
    guesses = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Game played by {self.player_name} on {self.timestamp}"
