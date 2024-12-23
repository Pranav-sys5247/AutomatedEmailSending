from django.http import HttpResponse
from django.shortcuts import render
from .forms import birthday

def home(request):
    if request.method == 'POST':
        # Pass both POST and FILES data to the form
        form = birthday(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the data to the database
            return render(request,"success.html")
    
        else:
            return render(request,"failure.html")
    else:
        form = birthday()  # Empty form for GET request
    return render(request, "autoemail.html", {'form': form})
