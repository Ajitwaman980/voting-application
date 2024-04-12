from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Voter(models.Model):
    PARTY_CHOICES = [
        ('BJP', 'BJP'),
        ('CONGRESS', 'Congress'),
        ('AAP', 'AAP'),
        ('SHIVSENA', 'Shivsena')
    ]

    aadhar = models.CharField(max_length=12, unique=True)
    vote = models.CharField(max_length=20, choices=PARTY_CHOICES)

    def __str__(self):
        return self.aadhar
