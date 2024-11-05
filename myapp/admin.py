from django.contrib import admin
from .models import Season, Ingredient,Flavour,CustomerSuggestion
# Register your models here.
@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields=('name',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display=('name','quantity','unit','allergen')
    list_filter=('allergen',)
    search_fields=('name',)

@admin.register(Flavour)
class FlavourAdmin(admin.ModelAdmin):
    list_display=('name','season','is_active')
    list_filter=('season','is_active')
    search_fields=('name','description')

@admin.register(CustomerSuggestion)
class CustomerSuggestionAdmin(admin.ModelAdmin):
    list_display=('customer_name','flavour_name')
    search_fields=('customer_name',)
