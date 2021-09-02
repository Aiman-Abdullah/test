from django.shortcuts import render
# test comment
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

#test
# Create your views here:
def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('dim_accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'dim_accounts/signup.html', {'form':form})
        
def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
        # log in the user
            user = form.get_user()
            login(request, user)
            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            # else:
            #     return redirect('/employee/list/')
            return redirect('/employee/list/')
    else:
         form = AuthenticationForm()
    return render(request, 'dim_accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/dim_accounts/signup/')

