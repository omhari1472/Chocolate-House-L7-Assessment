
from django.urls import path,include
from . import views
app_name='myapp'
urlpatterns = [
    path('', views.FlavorListView.as_view(), name='flavor-list'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient-list'),
    path('suggest/', views.CustomerSuggestionCreateView.as_view(), name='suggest-flavor'),
    

   

    path("__reload__/", include("django_browser_reload.urls")),
]
