from rest_framework import serializers
from django.contrib.auth.models import User
from luminarapi.models import Courses,DemoClass,Details,Modules,Batch,Overview,Attendance,Assignment,Announcement,LiveClass,VideoScreen,Test,JobPortal,Userprofile

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
class CourseSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model =Courses 
        fields = ['id', 'name', 'image']
class DemoSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=DemoClass
        fields=['id','name','thumbnail']
class DetailsSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model = Details
        fields = ['id','title','description','duration','online_fees','offline_fees','thumbnail']
class ModulesSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model =Modules
        fields = '__all__'
class BatchSerializer(serializers.ModelSerializer):
     id=serializers.CharField(read_only=True)
     class Meta:
         model=Batch
         fields="__all__"
class OverviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
         model=Overview
         fields="__all__"
class AttendanceSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Attendance
        fields="__all__"
class AssignmentSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Assignment
        fields="__all__"
class AnnouncementSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Announcement
        fields="__all__"
class LiveClassSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=LiveClass
        fields="__all__"
class VideoScreenSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=VideoScreen
        fields="__all__"
class TestSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Test
        fields="__all__"
class JobPortalSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=JobPortal
        fields="__all__"
class UserProfileSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Userprofile
        fields="__all__"





   


