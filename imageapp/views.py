from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .forms import ImageForm

def image_list(request):
    images = Image.objects.all()
    return render(request, 'imageapp/read.html', {'images': images})

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'imageapp/detail.html', {'image': image})

def image_create(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'imageapp/create.html', {'form': form})

def image_update(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm(instance=image)
    return render(request, 'imageapp/create.html', {'form': form})

def image_delete(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == "POST":
        image.delete()
        return redirect('image_list')
    return render(request, 'imageapp/delete.html', {'image': image})
