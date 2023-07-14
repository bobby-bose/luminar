from django.db import models
from django.contrib.auth.models import User



class Courses(models.Model):
    name=models.CharField(max_length=300)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    def __str__(self):
        return self.name
class DemoClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url_link = models.URLField()
    thumbnail = models.ImageField(upload_to='thumbnails')

    def __str__(self):
        return self.name
class Details(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration=models.CharField(max_length=300,default="6 months")
    offline_fees = models.DecimalField(max_digits=10, decimal_places=2)
    online_fees = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='thumbnails')


    def __str__(self):
        return self.title
class Modules(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails')
    
    
    mod1_text = models.TextField()
    mod2_text = models.TextField()
    mod3_text = models.TextField(blank=True,null=True)
    mod4_text = models.TextField(blank=True,null=True)
    mod5_text = models.TextField(blank=True,null=True)
    mod6_text = models.TextField(blank=True,null=True)
    mod7_text = models.TextField(blank=True,null=True)
    mod8_text = models.TextField(blank=True,null=True)
    mod9_text = models.TextField(blank=True,null=True)
    mod10_text = models.TextField(blank=True,null=True)
   
   
    

    def __str__(self):
        return self.title
class Batch(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    offline = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Overview(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    batch_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=255)
    subjects = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    batch_name = models.CharField(max_length=255)
    class_attended = models.IntegerField(default=0)
    total_classes = models.IntegerField(default=0)

    def __str__(self):
        return self.batchname
class Assignment(models.Model):
    task_name = models.CharField(max_length=255)
    date = models.DateField()
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
class LiveClass(models.Model):
    batch_name=models.CharField(max_length=300)
    trainer_name=models.CharField(max_length=300)
    time=models.TimeField()
    status=models.BooleanField(default=True)
    url_link=models.URLField()

    def __str__(self) :
        return self.batch_name
class VideoScreen(models.Model):
    course_name=models.CharField(max_length=300)
    description=models.CharField(max_length=500)
    date=models.DateField()
    def __str__(self):
        return self.course_name
class Test(models.Model):
    batch_name=models.CharField(max_length=300)
    test_title=models.CharField(max_length=300)
    date=models.DateField()
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
    












