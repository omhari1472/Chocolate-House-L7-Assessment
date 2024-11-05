from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
# Create your models here.
class Season(models.Model):
    name=models.CharField(max_length=50)
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-start_date']

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=20)  # e.g., kg, liters, pieces
    allergen = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

class Flavour(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    season=models.ForeignKey(Season,on_delete=models.CASCADE)
    ingredients=models.ManyToManyField(Ingredient,related_name="flavors")
    is_active=models.BooleanField(default=True)
   

    def __str__(self):
        return self.name
    
    def get_allergens(self):
        return self.ingredients.filter(allergen=True)


class CustomerSuggestion(models.Model):
    customer_name=models.CharField(max_length=50)
    flavour_name=models.CharField(max_length=50)
    description=models.TextField()
    allergies=models.TextField(blank=True,help_text="Any Concernson ")
    
    def __str__(self):
        return f"{self.flavour_name} suggested by {self.customer_name}"


