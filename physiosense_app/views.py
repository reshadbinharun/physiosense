from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage    

# Create your views here.
def test(request):
    return render(request, 'test.html', {})

def image(request):
    if request.method == 'POST' and request.FILES['image']:
        results_arr = []
        imagefile = request.FILES['image']
        print(imagefile)
        fs = FileSystemStorage()
        filename = fs.save(imagefile.name, imagefile)
        file_url = fs.url(filename)
        return render(request, 'image.html', {})