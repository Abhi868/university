

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator


class Classroom(models.Model):
        name=models.CharField(max_length=10, null=False,blank=False)
        seating_capacity=models.IntegerField()
        shapes=(('Oval','Oval'),('rectangular','rectangular'),('canopy','canopy'),('elevated','elevated'))
        shape=models.CharField(max_length=12,choices=shapes)
        BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
        web_support=models.BooleanField(choices=BOOL_CHOICES, default=False)
        teacher= models.ForeignKey('Teacher',related_name='teacher' , on_delete=models.CASCADE)
        def __str__(self):
                return self.name
	

class Subject(models.Model):
        subject_name=models.CharField(max_length = 20, null=False,blank=False)
        no_of_chapters=models.IntegerField()
        total_duration=models.CharField(max_length=10)
        duration_per_class=models.PositiveIntegerField(validators=[MinValueValidator(.5), MaxValueValidator(2)])
        classroom= models.ForeignKey(Classroom ,related_name='classroom' , on_delete=models.CASCADE)
        def __str__(self):
	        return self.subject_name

class Teacher(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    join_date=models.DateField()
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    salary=models.CharField(max_length=10 ,help_text='Enter in LPA ')
    subject=models.ForeignKey(Subject , related_name='subject', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Relatives(models.Model):
        name=models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
        related_to=models.OneToOneField(User, on_delete=models.CASCADE)
        relation=models.CharField(max_length=20)                
        phone_no=models.CharField(max_length=10,validators=[RegexValidator(regex='^.{10}$', message='Number has to be 10 digit', code='nomatch')])
        def __str__(self):
                return self.name.username

class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    join_date=models.DateField(auto_now_add=True)
    standard=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    roll_no=models.PositiveIntegerField(unique=True)
    ranking=models.PositiveIntegerField(unique=True)
    student_class=models.ForeignKey(Classroom ,related_name='s_classroom' , on_delete=models.CASCADE)
    def __str__(self):
         return self.user.username


	#def create(self):
	#	return self.seating_capcaity-=1


