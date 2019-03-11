from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RecipeModel, RecipeForm, UserModel, UserForm
from django.contrib.auth.models import User

# function at homepage to authenticate user.
def index(request):
    allEntries = RecipeModel.objects.all()
    context = {
        "allEntries": allEntries
    }
    return render(request, 'CodeSchoolRecipeApp/index.html', context)

# function renders form for new users
def createUser(request):
    newForm = UserForm(request.POST or None)
    if newForm.is_valid():
        newForm.save()
        return redirect('index')

    return render(request, 'CodeSchoolRecipeApp/createUser.html', {'userform':newForm})

# function used to edit user information
def editUser(request, username):
    # grab user from UserModel
    editExistingUser = get_object_or_404(UserModel, pk=username)
    # post information
    if request.method == "POST":
        form = UserForm(request.POST, instance=editExistingUser)
        # if information is valid
        if form.is_valid():
            # save form
            form.save()
        #     if not, say it is not valid
        else:
            print("form is not valid")
        return redirect('index')


    form = UserForm(instance=editExistingUser)
    context = {
         "form": form,
        "username": username  }
    return render(request, "CodeSchoolRecipeApp/editUser.html", context)



# function to create new recipe -- POST Request
def newRecipe(request):
    # If the form is being pushed to this function
    if request.method == "POST":
        print(request.method)
        # Put user information into new form variable
        form = RecipeForm(request.POST)
        # Check validation of form
        if form.is_valid():
            # Save the form's information in the model
            form.save()
            # Create a new Django User entry
            User.objects.create_user(request.POST["username"], "", request.POST["password1"])
            return redirect("index")
        else:
            context={
                "errors": form.errors,
                "form": form
            }
            return render(request, "CodeSchoolRecipeApp/newRecipe.html", context)
    # GET Request
    else:
        # This will create a blank form using RecipeForm
        form = RecipeForm()
        context = {"form": form}
        return render(request, "CodeSchoolRecipeApp/newRecipe.html", context)


# function displays all recipes in database
def allRecipes(request):
       recipe_list = RecipeModel.objects.all()
       context = {'recipe_list': recipe_list}
       return render(request, 'CodeSchoolRecipeApp/allRecipes.html', context)
          
# function that renders profile page
def profile(request):
    user_list = UserModel.objects.all()
    context = {'user_list': user_list}
    return render(request, 'CodeSchoolRecipeApp/profile.html', context)

# function that allows edit or update to recipes
def editRecipe(request, nameOfMeal):
    # Grab an exact entry of the recipeModel using the primary key
    editExistingRecipe = get_object_or_404(RecipeModel, pk=nameOfMeal)

    # Post method
    if request.method == "POST":
        # To put user's information in form and use the exact RecipeModel with primary key
        form = RecipeForm(request.POST, instance=editExistingRecipe)
        if form.is_valid():
            form.save()
        else:
            print("Form is not valid")
        return redirect("index")

    # Get exact recipe form using the existing recipe model using the primary key
    form = RecipeForm(instance=editExistingRecipe)
    context = {
        "form": form,
        "nameOfMeal": nameOfMeal
    }
    return render(request, "CodeSchoolRecipeApp/editRecipe.html", context)

# function that grabs info for user to edit
def gotEditRecipeInfo(request):
    # Creating new form variable
    form = UserForm(request.POST)
    # Putting the logged in user entry into the UserModel variable
    user = UserModel.objects.get(username=request.user)

    # Create a recipe from the logged in user
    if form.is_valid():
        # Created a new RecipeModel entry using the user's form information that was passed using the request.POST
        RecipeModel.objects.create(shortDescription=request.POST["shortDescription"], ingredients=request.POST["ingredients"],
                                   directions =request.POST["directions"], nameOfMeal=request.POST["nameOfMeal"],
                                   mealPicture=request.POST["mealPicture"], dateCreated=request.POST["dateCreated"])
        return redirect("index")
    else:
        context = {"form":form, "errors":form.errors}
        return render(request, "CodeSchoolRecipeApp/index.html", context)

# function to delete recipes in database
def deleteRecipe(request, nameOfMeal):
    deleteThisRecipe = get_object_or_404(RecipeModel, pk=nameOfMeal)
    deleteThisRecipe.delete()
    return redirect("index")
    