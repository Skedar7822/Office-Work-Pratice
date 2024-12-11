from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == 'POST':
        Form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) 
    pass

def login(request):
    pass
def dashboard(request):
    pass
def logout(request):
    pass
