import json
from django.http.response import JsonResponse
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  # import
from django.contrib.auth import authenticate, logout
# from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth.models import User, auth
from .models import postedJob, User #userData
# from datetime import timezone
from django.utils import timezone



@csrf_exempt
def signup(request):
    if request.method == 'POST':

        signInData = json.loads(request.body)

        user_name = signInData['username']
        first_N = signInData['first_name']
        last_N = signInData['last_name']
        e_Mail = signInData['email']
        dofb = signInData['dob']
        contact = signInData['contact']
        pass_word = signInData['password']

        if User.objects.filter(userName=user_name).exists():
            print("Username Taken")
            return JsonResponse({
                "success": False,
                "error": "User name Taken"
            })
        elif User.objects.filter(email=e_Mail).exists():
            print("Email already Exist")
            return JsonResponse({
                "success": False,
                "error": "Email already Exist"
            })
        elif User.objects.filter(contactNumber=contact).exists():
            print("Mobile already Exist")
            return JsonResponse({
                "success": False,
                "error": "Mobile already Exist"
            })
            
        else:
            user = User.objects.create_user(
                password=pass_word,
                userName=user_name,
                firstName=first_N,
                lastName=last_N,
                email=e_Mail,
                dob=dofb,
                contactNumber=contact,
            )
            user.save()

            userInfo = {
                'User Name': user_name,
                'First Name': first_N,
                'Last Name': last_N,
                'E-Mail': e_Mail,
                'Date of Birth': dofb,
                'Contact': contact,
                'success': True
            }
            print("Data Saved")
            return JsonResponse(userInfo)
    else:
        print('Error')
        return JsonResponse({
            "success": False,
            "error": "Unknown error"
        })

# "email": "jashsharma@gmail.com",
# "contactNumber": "8319828866",

@csrf_exempt
def login(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        if "userName" in jsonData.keys():

            user = authenticate(
                userName=jsonData['userName'],
                password=jsonData['password']
            )

            if user is not None:
                request.session['user'] = jsonData['userName']
                return JsonResponse({
                    "success": True,
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Username or Password Wrong"
                })
                
        elif "email" in jsonData.keys():          
            
            try:
                userInfoByEmail = User.objects.get(email=jsonData['email'])
            except:
                return JsonResponse({"Error": "No User Found"})

            print(userInfoByEmail.userName)
            user = authenticate(
                userName=userInfoByEmail.userName,
                password=jsonData['password']
            )

            if user is not None:
                request.session['user'] = userInfoByEmail.userName
                return JsonResponse({
                    "success": True,
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Email or Password Wrong"
                })
                     
        else:
            try:
                userInfoByCont = User.objects.get(
                    contactNumber=jsonData['contactNumber'])
            except:
                return JsonResponse({"Error": "Cont No User Found"})
            user = authenticate(
                userName=userInfoByCont.userName,
                password=jsonData['password'])
            if user is not None:
                request.session['user'] = userInfoByCont.userName
                return JsonResponse({
                    "success": True,
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Contact Number or Password Wrong"
                })

    else:
        return JsonResponse({
            "success": False,
            "error": "No Request"
        })

@csrf_exempt
def user(request):
    return JsonResponse({
        "User": request.session.get('user')
    })

@csrf_exempt
def logouts(request):
    logout(request)
    return JsonResponse({
        "User": "None"
    })

@csrf_exempt
def userProfile(request, userID):
    try:
        print(userID)
        userInformation = User.objects.get(userName=userID)
        return JsonResponse({
            "success": True,
            "Data": {
                'userName': userInformation.userName,
                'firstName': userInformation.firstName,
                'lastName': userInformation.lastName,
                'email': userInformation.email,
                'dob': userInformation.dob,
                'contactNumber': userInformation.contactNumber,
                'address': userInformation.address,
                'city': userInformation.city,
                'state': userInformation.state,
                'bio': userInformation.bio,
                'skills': userInformation.skills,
                'projects': userInformation.projects,
                'linkGithub': userInformation.linkGithub,
                'linkLinkedIn': userInformation.linkLinkedIn,
                'linkExtra': userInformation.linkExtra,
            }
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            "success": False,
            "error": "User not found"
        })

@csrf_exempt
def postJob(request):

    if request.method == 'POST':
        jobData = json.loads(request.body)
        job = postedJob(
            title=jobData['title'],
            jobPos=jobData['jobPos'],
            desc=jobData['desc'],
            timing=jobData['timing'],
            reqSkill=jobData['reqSkill'],
            expLevel=jobData['expLevel'],
            postedBy=request.session.get('user'),
            location=jobData['location'],
        )
        job.save()
        print(jobData['reqSkill'])
        return JsonResponse({
            "success": True,
            "Data": {
                "title": jobData['title'],
                "jobPos": jobData['jobPos'],
                "desc": jobData['desc'],
                "timing": jobData['timing'],
                "reqSkill": jobData['reqSkill'],
                "expLevel": jobData['expLevel'],
                "location": jobData['location']
            }
        })
        
    return JsonResponse({
        "success": True,
    })

@csrf_exempt
def apply(request,jobPostID):

     
    currUser = request.session.get('user')
    postedJobData = postedJob.objects.get(id = jobPostID)
    
    # applicants = dict(postedJobData.appliedPeople)
    
    print(postedJobData.appliedPeople)
    # print(applicants.ID)
    
    userProfileData = User.objects.get(userName = currUser)
    print(userProfileData.firstName)
    return JsonResponse({"ID" : userProfileData.id})