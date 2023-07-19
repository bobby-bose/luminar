"""
URL configuration for luminar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from luminarapi import views as api_view




from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("api/register",api_view.UsersView,basename="users"),
router.register("api/courses",api_view.CoursesListView,basename="courses"),
router.register("api/democlass",api_view.DemoClassListView,basename="democlass"),
router.register("api/details",api_view.DetailsListAPIView,basename="details"),
router.register("api/modules",api_view.ModulesAPIView,basename="modules"),
router.register("api/batches",api_view.BatchListView,basename="batches"),
router.register("api/overview",api_view.OverDetailView,basename="overview"),
router.register("api/attendance",api_view.AttendanceView,basename="attendance"),
router.register("api/assignment",api_view.AssignmentView,basename="assignment"),
router.register("api/announcement",api_view.AnnouncementView,basename="announcement"),
router.register("api/liveclass",api_view.LiveClassView,basename="liveclass"),
router.register("api/videoscreen",api_view.VideoScreenView,basename="videoscreen"),
router.register("api/test",api_view.TestView,basename="test"),
router.register("api/jobportal",api_view.JobPortalView,basename="jobportal"),
router.register("api/userprofile",api_view.UserProfileView,basename="userprofile"),



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/token/",ObtainAuthToken.as_view()),
    path("api/sendpassword/",api_view.SendPassword),

    path('api/password-reset/<int:id>/',api_view.PasswordReset),
    path("api/verifyotp/<int:id>/", api_view.VerifyOtp),
     path("api/resetpassword/<int:id>/", api_view.Resetpassword),


    
    
   
    path("", include(router.urls))

   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+router._urls