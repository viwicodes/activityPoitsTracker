from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . models import Cerficate

# Image processing
import pytesseract as tess
from PIL import Image

# Create your views here.
    
@csrf_exempt
def upload(request):
    if request.method == "POST":
        if request.user.student_profile.role == 'student':
            file = request.FILES.get("file")
            # Add certificate to db
            Cerficate.objects.create(owner=request.user.student_profile.user, file=file)

            # Get last uploaded file
            curr = Cerficate.objects.filter(owner = request.user.student_profile.user)
            last_uploaded = curr.latest('updated_at').file.url # Last uploaded url
            img_url = ".{}".format(last_uploaded)
            img = Image.open(img_url) # Image for processing
            text = tess.image_to_string(img) # Extracted text
            category = "Internship" # Check category

            # check for category
            if category.lower() in text.lower():
                print(category)
            else:
                print("Word not found")
            
            return HttpResponse("File added")
        elif request.user.teacher_profile.role == 'teacher':
            return HttpResponse("You can't upload {}, beacause you are a {}.".format(request.user.username, request.user.teacher_profile.role))

    else:
        current = Cerficate.objects.filter(owner = request.user.student_profile.user)
        return HttpResponse(current[3].file.url)
