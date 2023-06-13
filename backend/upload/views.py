from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . models import Cerficate
from django.db.models import Sum
from django.core import serializers



# Image processing
import pytesseract as tess
from PIL import Image

# Create your views here.
    
@csrf_exempt
def upload(request):
    points = 0
    # user = request.user
    if request.method == "POST":
        if request.user.student_profile.role == 'student':
            file = request.FILES.get("file")
            # Add certificate to db
            Cerficate.objects.create(owner=request.user.student_profile.user, file=file)

            # Get last uploaded file
            filtered_set = Cerficate.objects.filter(owner = request.user.student_profile.user)
            last_uploaded = filtered_set.latest('updated_at') # Last uploaded Entry
            img_url = ".{}".format(last_uploaded.file.url)
            img = Image.open(img_url) # Image for processing
            text = tess.image_to_string(img) # Extracted text
            category = ["Internship", "Sports", "Arts"] # Check category

            # check for category
            for each in category:
                # print(request.user.student_profile.name)
                if each.lower() in text.lower():
                    last_uploaded.points = 10
                    last_uploaded.save()
                    aggregate_set = Cerficate.objects.filter(owner = last_uploaded.owner)
                    total = aggregate_set.aggregate(Sum('points'))['points__sum']
                    request.user.student_profile.points = total
                    request.user.save()
                    return HttpResponse(total)
                else:
                    print("Word not found")
            
            return HttpResponse("File added")
        elif request.user.teacher_profile.role == 'teacher':
            return HttpResponse("You can't upload {}, beacause you are a {}.".format(request.user.username, request.user.teacher_profile.role))

    else:
        current = Cerficate.objects.filter(owner = request.user.student_profile.user)
        return HttpResponse(current[3].file.url)

# Frontend APIs
def getStudentCertificate(request):
    if request.method == "GET":
        current_user = request.user.student_profile
        if current_user:
            username = current_user.user.username
            data = []
            filtered_row = Cerficate.objects.filter(owner = username)
            for each in filtered_row:
                data.append({
                    "owner":each.owner,
                    "file":each.file.url,
                    "points":each.points
                })
            res = JsonResponse(data, safe=False)
            return res