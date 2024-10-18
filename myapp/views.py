from django.shortcuts import render
from django.http import HttpResponse
from .forms import Imageform
from .models import Image
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Image uploaded successfully!')  # Success message after valid form
        # else:
            # messages.error(request, 'There was an error uploading the image.')  # Error message if form is invalid
    else:
        form = Imageform()
    img = Image.objects.all()
    return render(request, "home.html", {'img':img ,'form': form})
