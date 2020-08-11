from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def simple_upload(request):
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        return render(request,'MyApp/SimpleUp.html',{'uploaded_file_url':uploaded_file_url})
    return render(request,'MyApp/SimpleUp.html')