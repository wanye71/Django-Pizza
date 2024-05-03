from django.db import models

class Size(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.size} Pizza with {self.topping1} and {self.topping2}"