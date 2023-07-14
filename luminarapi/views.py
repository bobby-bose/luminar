from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin
from rest_framework import authentication,permissions
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from luminarapi.serializers import UserSerializer,CourseSerializers,DemoSerializers,DetailsSerializer,ModulesSerializer,BatchSerializer,OverviewSerializer,AttendanceSerializer,AssignmentSerializer,AnnouncementSerializer,LiveClassSerializer,VideoScreenSerializer
from luminarapi.models import Courses,DemoClass,Details,Modules,Batch,Overview,Attendance,Assignment,Announcement,LiveClass,VideoScreen
from luminarapi.serializers import TestSerializer,JobPortalSerializer,UserProfileSerializer
from luminarapi.models import Test,JobPortal,Userprofile
class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=get_user_model().objects.all()
    model=User
    http_method_names=["post","get"]
class CoursesListView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializers
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get","put"]
    def list(self, request, *args, **kwargs):
        try:
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)


    
class DemoClassListView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin):
    queryset=DemoClass.objects.all()
    serializer_class=DemoSerializers
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get","put"]
    def list(self, request, *args, **kwargs):
        try:
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
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
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)

class ModulesAPIView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin):
    queryset = Modules.objects.all()
    serializer_class =ModulesSerializer 
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get","put"]
    def list(self, request, *args, **kwargs):
        try:
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)

class BatchListView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset=Batch.objects.all()
    serializer_class=BatchSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
    def list(self, request, *args, **kwargs):
        try:
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)

class OverDetailView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=Overview.objects.all()
    serializer_class=OverviewSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
    def list(self, request, *args, **kwargs):
        try:
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)


class AttendanceView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    def list(self, request, *args, **kwargs):
        try:
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)
    http_method_names=["post","get"]
    def list(self, request, *args, **kwargs):
        try:
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)

class AssignmentView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
    def list(self, request, *args, **kwargs):
        try:
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
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
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)

class LiveClassView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=LiveClass.objects.all()
    serializer_class=LiveClassSerializer
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post"]
    def list(self, request, *args, **kwargs):
        try:
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
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
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
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
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
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
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
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
            courses = self.get_queryset()
            total_results = courses.count()

            if total_results == 0:
                # If there are no courses, set the status as "error"
                response_data = {
                    "status": "error",
                    "error_message": "No courses found.",
                    "totalResults": total_results
                }
            else:
                # If there are courses, set the status as "ok"
                serialized_courses = self.serializer_class(courses, many=True)
                response_data = {
                    "status": "ok",
                    "courses": serialized_courses.data,
                    "totalResults": total_results
                }
        except Exception as e:
            # If there is an exception, set the status as "error" and print the error message
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }
        
        return Response(response_data)


   
    
        

    



    
    
   

    


