from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views import View


class FileUploadView(View):

    @staticmethod
    def get(request):
        return render(request, "upload.html")

    @staticmethod
    def post(request):
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        return render(request, "upload.html", {"image_url": image_url})
