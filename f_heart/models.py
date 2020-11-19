from django.db import models

class Inquiries(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return self.email


class MembersOfProgram(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    #gender
    
    class Meta:
        verbose_name = 'Members of programs'
        verbose_name_plural = 'Members of Programs'

    def __str__(self):
        return self.email
    

