from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView
from .models import Flavour,Ingredient,CustomerSuggestion
from django.contrib import messages

# Create your views here.
class FlavorListView(ListView):
    model = Flavour
    temp_name='myapp/flavour_list.html'
    context_object_name = 'flavors'
    
    def get_queryset(self):
        return Flavour.objects.filter(is_active=True)
    
class IngredientListView(ListView):
    model = Ingredient
    temp_name = 'myapp/ingredient_list.html'
    context_object_name = 'ingredients'

class CustomerSuggestionCreateView(CreateView):
    model = CustomerSuggestion
    template_name = 'myapp/suggestion_form.html'
    fields = ['customer_name','flavour_name', 'description', 'allergies']
    success_url = '/'

# class SeasonalFlavorsView(ListView):
#     model = Flavour
#     template_name = 'myapp/seasonal_flavors.html'
#     context_object_name = 'flavors'  
#     def get_queryset(self):
#         selected_season = self.request.GET.get('season', 'spring')  
#         return Flavour.objects.filter(season__name=selected_season)  