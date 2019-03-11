from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('allRecipes/', views.allRecipes, name="allRecipes"),
    path('newRecipe/', views.newRecipe, name="newRecipe"),
    path('profile/', views.profile, name="profile"),
    path('createUser/', views.createUser, name="createUser"),
    path('gotEditRecipeInfo/', views.gotEditRecipeInfo, name="gotRecipeEditInfo"),
    path('editRecipe/<int:nameOfMeal>/', views.editRecipe, name="editRecipe"),
    path('editUser/<int:username>/', views.editUser, name="editUser"),
    path('deleteRecipe/<int:nameOfMeal>/', views.deleteRecipe, name="deleteRecipe"),
]
