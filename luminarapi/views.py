

import smtplib
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin
from rest_framework import authentication,permissions
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from luminarapi.serializers import UserSerializer,DemoSerializers,DetailsSerializer,BatchSerializer,OverviewSerializer,AttendanceSerializer,AssignmentSerializer,AnnouncementSerializer,LiveClassSerializer,VideoScreenSerializer
from luminarapi.models import DemoClass,Details,Batch,Overview,Attendance,Assignment,Announcement,LiveClass,VideoScreen
from luminarapi.serializers import TestSerializer,JobPortalSerializer,UserProfileSerializer,VideoScreenClassSerializer,LogoSerializer,ModuleSerializer
from luminarapi.models import Test,JobPortal,Userprofile,VideoScreenClass,Logo,Module

from twilio.rest import Client
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import permissions



def test(request):
    pass



class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=get_user_model().objects.all()
    model=User
    http_method_names=["post","get"]


    
class DemoClassListView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin):
    queryset=DemoClass.objects.all()
    serializer_class=DemoSerializers
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get","put"]
    def list(self, request, *args, **kwargs):
        try:
            democlass = self.get_queryset()
            total_results = democlass.count()

            if total_results == 0:
                
                
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
                
                serialized_demo_classes = self.serializer_class(democlass, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_demo_classes.data,
                    "totalResults": total_results
                }
        except Exception as e:
           
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
    
class DetailsListAPIView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get","put"]
    def list(self, request, *args, **kwargs):
        try:
            details = self.get_queryset()
            total_results = details.count()

            if total_results == 0:
                response_data = {
                    "status": "ok",
                    "message": [],
                    "totalResults": total_results
                }
            else:
                serialized_details = self.serializer_class(details, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_details.data,
                    "totalResults": total_results
                }
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": 0  # Reset totalResults on error
            }

        return Response(response_data)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data, status=201)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data, status=400)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }

        return Response(response_data)
    

    
class BatchListView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin):
    queryset=Batch.objects.all()
    serializer_class=BatchSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get","put"]
    def list(self, request, *args, **kwargs):
        try:
            batches = self.get_queryset()
            total_results = batches.count()

            if total_results == 0:
                
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
             
                serialized_batches = self.serializer_class(batches, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_batches.data,
                    "totalResults": total_results
                }
        except Exception as e:
           
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
class OverDetailView(GenericViewSet,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset=Overview.objects.all()
    serializer_class=OverviewSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get","put"]
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializered_course = self.serializer_class(instance)
            
            
            subjects_list = [subject.strip() for subject in instance.subjects.split(',')]
            
            response_data = {
                "status": "ok",
                "data": {
                    "id": serializered_course.data.get("id"),
                    "start_date":serializered_course.data.get("start_date"),
                    "batch_code": serializered_course.data.get("batch_code"),
                    "course_name": serializered_course.data.get("course_name"),
                    "subjects": subjects_list,
                  
                }
            }

        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }

        return Response(response_data)
   
    
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializered_course = self.serializer_class(instance)
            
            
            subjects_list = [subject.strip() for subject in instance.subjects.split(',')]
            
            response_data = {
                "status": "ok",
                "data": {
                    "id": serializered_course.data.get("id"),
                    "start_date":serializered_course.data.get("start_date"),
                    "batch_code": serializered_course.data.get("batch_code"),
                    "course_name": serializered_course.data.get("course_name"),
                    "subjects": subjects_list,
                  
                }
            }

        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }

        return Response(response_data)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
class AttendanceView(GenericViewSet,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post","put"]
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializered_course = self.serializer_class(instance)

            # Instead of manually specifying fields, you can use serializer.data to get the updated data
            response_data = {
                "status": "ok",
                "data": {
                    "id": serializered_course.data.get("id"),
              
                    "batch_name": serializered_course.data.get("batch_name"),
                      "class_attended": serializered_course.data.get("class_attended"),
                       "total_classes":serializered_course.data.get("total_classes"),

                    
                }
            }
            return Response(response_data)  # Use HTTP_200_OK constant
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)  # Use HTTP_400_BAD_REQUEST constant

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "status": "ok",
                "data": serializer.data,
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
    
    

    
class AssignmentView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get","put"]
    def list(self, request, *args, **kwargs):
        try:
            assignments = self.get_queryset()
            total_results = assignments.count()

            if total_results == 0:
               
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
                
                serialized_assignments = self.serializer_class(assignments, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_assignments.data,
                    "totalResults": total_results
                }
        except Exception as e:
           
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
class AnnouncementView(GenericViewSet,CreateModelMixin,ListModelMixin):
    queryset=Announcement.objects.all()
    serializer_class=AnnouncementSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
    def list(self, request, *args, **kwargs):
        try:
            announcements = self.get_queryset()
            total_results = announcements.count()

            if total_results == 0:
                
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
                
                serialized_announcements = self.serializer_class(announcements, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_announcements.data,
                    "totalResults": total_results
                }
        except Exception as e:
            
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
class LiveClassView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin):
    queryset=LiveClass.objects.all()
    serializer_class=LiveClassSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post","put"]
    def list(self, request, *args, **kwargs):
        try:
            live_classes = self.get_queryset()
            total_results = live_classes.count()

            if total_results == 0:
                
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
               
                serialized_live_classes = self.serializer_class(live_classes, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_live_classes.data,
                    "totalResults": total_results
                }
        except Exception as e:
            
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "status": "ok",
                "data": serializer.data,
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
    
class VideoScreenView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=VideoScreen.objects.all()
    serializer_class=VideoScreenSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post"]
    def list(self, request, *args, **kwargs):
        try:
            video_screens = self.get_queryset()
            total_results = video_screens.count()

            if total_results == 0:
               
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
                serialized_video_screens = self.serializer_class(video_screens, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_video_screens.data,
                    "totalResults": total_results
                }
        except Exception as e:
        
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": 0 
            }
        
        return Response(response_data)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
class TestView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=Test.objects.all()
    serializer_class=TestSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post"]
    def list(self, request, *args, **kwargs):
        try:
            tests = self.get_queryset()
            total_results = tests.count()

            if total_results == 0:
                
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
                
                serialized_tests = self.serializer_class(tests, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_tests.data,
                    "totalResults": total_results
                }
        except Exception as e:
            
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
class JobPortalView(GenericViewSet,CreateModelMixin,ListModelMixin):
    queryset=JobPortal.objects.all()
    serializer_class=JobPortalSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
    def list(self, request, *args, **kwargs):
        try:
            job_portals = self.get_queryset()
            total_results = job_portals.count()

            if total_results == 0:
                
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
                
                serialized_job_portals = self.serializer_class(job_portals, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_job_portals.data,
                    "totalResults": total_results
                }
        except Exception as e:
            
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
class UserProfileView(GenericViewSet, CreateModelMixin, ListModelMixin,UpdateModelMixin):
    queryset = Userprofile.objects.all()
    serializer_class = UserProfileSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post","put"]
    def list(self, request, *args, **kwargs):
        try:
            user_profiles = self.get_queryset()
            total_results = user_profiles.count()
            if total_results == 0:
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
                serialized_user_profiles = self.serializer_class(user_profiles, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_user_profiles.data,
                    "totalResults": total_results
                }
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
import random
from django.views.decorators.csrf import csrf_exempt
global_password = ""
@csrf_exempt
def SendPassword(request):
    if request.method == "POST":
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("luminartechnolab995@gmail.com", "rlovvscccjgzmqzw")
        
        email = request.POST.get("email")
        username = request.POST.get("username")
        mobile_number = request.POST.get("mobile_number")
        
        password = generate_password(username, mobile_number)
        global_password = password
        
        subject = 'Password Verification'
        from_email = 'luminartechnolab995@gmail.com'
        recipient_list = [email]
        
        html = render_to_string('email.html', {"variable": password})
        plain_message = strip_tags(html)
        server.sendmail(from_email, recipient_list, plain_message)
        
        return HttpResponse("POST called")
    
    return HttpResponse("Called")
def generate_password(username, mobile_number):
   
    username_first_four = username[:4]
    mobile_last_three = mobile_number[-3:]
    
    password = username_first_four + mobile_last_three
    return password
import random
import string
from luminarapi.models import User,Userprofile
@csrf_exempt
def PasswordReset(request, id):
    if request.method == "POST":
        
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return HttpResponse("User not found")
        otp_length = 6  
        otp = ''.join(random.choices(string.digits, k=otp_length))
        user.otp = otp
        user.save()
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        from_email='luminartechnolab995@gmail.com'
        server.login('luminartechnolab995@gmail.com','rlovvscccjgzmqzw')
        subject = 'OTP Verification'
        recipient_list = [user.email]
        html=render_to_string('password-reset.html',{"variable":otp})
        plain_message=strip_tags(html)
        message = f"Your OTP: {otp}"
        
        try:
            server.sendmail(from_email, recipient_list, plain_message)
        except Exception as e:
            print("Error sending email:", str(e))
            return HttpResponse("Failed to send OTP email")
        request.session['otp'] = otp
        print("Registered Email:", user.email)
        print("Registered Username:", user.username)
        print("OTP:", otp)
        
        return HttpResponse("POST called")
    
    return HttpResponse("Called")
def VerifyOtp(request, id):
    if request.method == 'POST':
        
        entered_otp = request.POST.get("user_otp")
        stored_otp = request.session.get("otp")
        

        print("-----------------")
        print( entered_otp, stored_otp)

        if entered_otp == stored_otp:
            try:
                user = User.objects.get(id=id)
                registered_email = user.email
                registered_username = user.username
                print(registered_email)
                print(registered_username)
           
           
                return HttpResponse('verified otp')
            except User.DoesNotExist:
                return HttpResponse("User not found")
        else:
            return HttpResponse("Invalid OTP. Please try again.")
    else:
        return HttpResponse("Invalid request method.")
def Resetpassword(request, id):
    if request.method == 'POST':
        entered_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        print(entered_password)

        if entered_password == confirm_password:
            try:
                user = User.objects.get(id=id)
                user.set_password(entered_password)
                user.save()

                registered_email = user.email
                registered_username = user.username
                registered_email = user.email
                registered_username = user.username
                response = f"Passwords match. Registered Email: {registered_email}, Registered Username: {registered_username}"
                return HttpResponse(response)
            except User.DoesNotExist:
                return HttpResponse("User not found")
        else:
            return HttpResponse("Passwords do not match. Please try again.")

    else:
        return HttpResponse("Invalid request method.")
class VideoScreenClassViewSet(GenericViewSet,CreateModelMixin,ListModelMixin,UpdateModelMixin,RetrieveModelMixin):
    queryset = VideoScreenClass.objects.all()
    serializer_class = VideoScreenClassSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        response_data = {
            "status": "ok",
            "data": serializer.data
        }
        return Response(response_data)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                "status": "ok",
                "data": serializer.data
            }
            return Response(response_data)
        
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "status": "ok",
                "data": serializer.data,
            }
            return Response(response_data)
        
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            if not serializer.data:  # Check if the data list is empty
                response_data = {
                    "status": "ok",
                    "data": []
                }
            else:
                response_data = {
                    "status": "ok",
                    "data": serializer.data
                }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }
            return Response(response_data)
class LogoViewSet(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    http_method_names=['get','post','put']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        response_data = {
            "status": "ok",
            "data": serializer.data
        }
        
        return Response(response_data)
    
class ModuleView(GenericViewSet,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,ListModelMixin):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    http_method_names=['get','post','put']
    def list(self, request, *args, **kwargs):
        try:
            user_profiles = self.get_queryset()
            total_results = user_profiles.count()

            if total_results == 0:
                response_data = {
                    "status": "ok",
                    "message": "[]",
                    "totalResults": total_results
                }
            else:
                serialized_user_profiles = self.serializer_class(user_profiles, many=True)
                response_data = {
                    "status": "ok",
                    "data": serialized_user_profiles.data,
                    "totalResults": total_results
                }
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }

        return Response(response_data)
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            response_data = {
                "status": "ok",
                "data": serializer.data
            }
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }

        return Response(response_data)
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "status": "ok",
                "data": serializer.data
            }
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }

        return Response(response_data)
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                "status": "ok",
                "data": serializer.data
            }
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e)
            }

        return Response(response_data)