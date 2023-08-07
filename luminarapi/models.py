from django.db import models
from django.contrib.auth.models import User

class DemoClass(models.Model):
    name = models.CharField(max_length=100)
    
    thumbnail = models.ImageField(upload_to='thumbnails')

    def __str__(self):
        return self.name
class VideoScreenClass(models.Model):
    name=models.ForeignKey(DemoClass,on_delete=models.DO_NOTHING)
    description=models.TextField()
    video_link=models.URLField()
    uploaded_date=models.CharField(max_length=10)
class Details(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration=models.CharField(max_length=300,default="6 months")
    offline_fees = models.DecimalField(max_digits=10, decimal_places=2)
    online_fees = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='thumbnails')
    full_name=models.CharField(max_length=100,default=False)
    cochin=models.CharField(max_length=100,default=False)
    calicut=models.CharField(max_length=100,default=False)
    def __str__(self):
        return self.title
    
    def modules(self):
       
        return self.module_set.all()
    
class Module(models.Model):
    name=models.ForeignKey(Details,on_delete=models.DO_NOTHING, null=True, blank=True)
    mod_no=models.PositiveIntegerField()
    mod_heading=models.CharField(max_length=100)
    mod_description=models.CharField(max_length=600)

class Batch(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    offline = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Overview(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.CharField(max_length=10)
    batch_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=255)
    subjects = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Attendance(models.Model):
    batch_name = models.CharField(max_length=255)
    class_attended = models.IntegerField(default=0)
    total_classes = models.IntegerField(default=0)
    monthly_attedance=models.IntegerField(default=0)

    def __str__(self):
        return self.batchname
class Assignment(models.Model):
    task_name = models.CharField(max_length=255)
    date = models.CharField(max_length=10)
    time = models.TimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.task_name
class Announcement(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    date=models.DateField()
    def __str__(self) :
        return self.title

 

   
class VideoScreen(models.Model):
    course_name=models.CharField(max_length=300)
    description=models.CharField(max_length=500)
    date=models.DateField()
    link=models.URLField(null=True,default="")
    thumbnail=models.ImageField(upload_to="thumbnails",default="")
    
    def __str__(self):
        return self.course_name
class Test(models.Model):
    batch_name=models.CharField(max_length=300)
    test_title=models.CharField(max_length=300)
    date=models.CharField(max_length=100)
    total_mark=models.PositiveIntegerField(default=100)
    obtained_mark=models.PositiveIntegerField()
    def __str__(self):
        return self.batch_name
class JobPortal(models.Model):
    Job_title=models.CharField(max_length=300)
    location=models.CharField(max_length=200,default="eranakulam")
    salary=models.PositiveIntegerField()
    bond=models.PositiveIntegerField()
    url_link=models.URLField()
    def __str__(self):
        return self.Job_title
class Userprofile(models.Model):
    user_name=models.CharField(max_length=300)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    def __str__(self) :
        return self.user_name
class Logo(models.Model):
    image=models.ImageField(upload_to="image")

class LiveClass(models.Model):
    batch_name=models.CharField(max_length=300)
    trainer_name=models.CharField(max_length=300)
    time=models.TimeField()
    status=models.BooleanField(default=True)
    url_link=models.URLField()
    logo = models.ForeignKey(Logo, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self) :
        return self.batch_name







    












