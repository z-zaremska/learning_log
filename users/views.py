from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registration of new users."""
    if request.method != 'POST':
        #Blank formula for user registration
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #Log in new user and return to main page
            login(request, new_user)
            return redirect('learning_logs:index')
    
    #Prints blank formula
    context = {'form': form}
    return render(request, 'registration/register.html', context)

