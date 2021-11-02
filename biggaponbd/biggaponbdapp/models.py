from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name =models.CharField(max_length=15)

    def __str__(self):
        return self.category_name

class ToLetCategory(models.Model):
    tolet_category_name =models.CharField(max_length=15)

    def __str__(self):
        return self.tolet_category_name

class Userpost(models.Model):
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, upload_to='picture', default='tolet.png')
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=14)
    details = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    tolet_category =models.ForeignKey(ToLetCategory, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering =['-posted_date']

class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    profileImg =models.ImageField( upload_to='profile_picture' ,default='no_img.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

class TopAdd(models.Model):
    TopaddImg =models.ImageField(upload_to='Topadd Picture')
    title = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class Caro(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class HonerProfile(models.Model):
    img=models.ImageField(upload_to='HonerProfilePicture')
    name=models.CharField(max_length=30)
    education = models.CharField(max_length=50)
    skill=models.CharField(max_length=100)
    profession=models.CharField(max_length=30)
    contruct=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contuct(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone =models.CharField(max_length=15)
    email =models.EmailField(max_length=50)
    message =models.TextField()

    def __str__(self):
        return self.name +' , '+ self.email

