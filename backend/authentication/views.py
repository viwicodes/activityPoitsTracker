from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth


# Register User


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        semester = request.POST.get('semester')
        points = request.POST.get('points')
        role = request.POST.get('role')

        if password == confirmPassword:

            if role == 'student':
                User.objects.create_user(username=username, password=password)
                user = User.objects.get(username=username)
                user.student_profile.name = name
                user.student_profile.email = email
                user.student_profile.ph = phone
                user.student_profile.sem = semester
                user.student_profile.points = points
                user.student_profile.role = role
                user.teacher_profile.role = "not"
                user.save()
                return HttpResponse("Student added")
            
            if role == 'teacher':
                User.objects.create_user(username=username, password=password)
                user = User.objects.get(username=username)
                user.teacher_profile.name = name
                user.teacher_profile.email = email
                user.teacher_profile.ph = phone
                user.teacher_profile.sem = semester
                user.teacher_profile.points = points
                user.teacher_profile.role = role
                user.student_profile.role = "not"
                user.save()
                return HttpResponse("Teacher added")
            
        else:
            return HttpResponse("Password Mismatch")
        # return HttpResponse(username, password)
    else:
        return HttpResponse("Not POST")



# Login User
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password == confirmPassword:
            
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                if user.teacher_profile.role == "teacher":
                    return HttpResponse("Hello {}, you are a {}".format(user.teacher_profile.name, user.teacher_profile.role))
                elif user.student_profile.role == "student":
                    return HttpResponse("Hello {}, you are a {}".format(user.student_profile.name, user.student_profile.role))
            else:
                return HttpResponse("User does no exist.")
            
        else:
            return HttpResponse("Password Mismatch")
    else:
        return HttpResponse("Not a post request")
    
@csrf_exempt
def upload(request):
    if request.method == "POST":
        if request.user.student_profile.role == 'student':
            return HttpResponse(request.user.student_profile.role)
        elif request.user.teacher_profile.role == 'teacher':
            return HttpResponse("You can't upload {}, beacause you are a {}.".format(request.user.username, request.user.teacher_profile.role))
        