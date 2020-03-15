from django.shortcuts import render
from myschool import models
# Create your views here.
from django.views import View
class get_classroom_data(View):
    def get(self,request):
        print('inside get classroom')
        data=models.Classroom.objects.select_related().all()
        return render(request,'home.html',{'data':data})


def get_list_of_students(request):
    Students.objects.filter(request.user.id)