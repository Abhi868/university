from django.shortcuts import render
from myschool import models
from django.db.models import Prefetch
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.db.models import Count,Sum

# Create your views here.
from django.views import View
class get_classroom_data(View):
    def get(self,request):
        print('inside get classroom')
        data=models.Classroom.objects.prefetch_related('classroom').select_related('teacher').all()
        return render(request,'home.html',{'complete_data':data})


@csrf_exempt
class search_for_teacher(View):
    def post(self,request):
        try:
            teacher_name =request.POST.get('search_for')
            classroom_ids = models.Teacher.objects.select_related('subject__classroom').filter(name=techer_name).values_list('subject__classroom',flat=True)
            data = models.Student.objects.filter(stu_classes__in=classroom_ids).values_list('id','roll_no','ranking','standard','student_class__name')
            new_data=[(d) for d in data]     
            return HttpResponse(json.dumps({'status':200,'response_data':new_data}))
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return HttpResponse(json.dunps({'status':404,'response_message':'No such teacher found'}))
    def get(self,request):
        return HttpResponse({'status':403,'response_message':'This method is not allowed'})

@csrf_exempt
def get_list_of_students(request):
	try:
		teacher_name =request.POST.get('search_for')
		print('teacher name',teacher_name)
		classroom_ids = models.Teacher.objects.filter(user__username=teacher_name).values_list('subject__classroom_id',flat=True)
		print(classroom_ids)
		data = models.Student.objects.filter(student_class__in=classroom_ids).values_list('id','user__username','roll_no','ranking','standard','student_class__name')
		new_data=[(d) for d in data]     
		return HttpResponse(json.dumps({'status':200,'response_data':new_data}))
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno)
		return HttpResponse(json.dunps({'status':404,'response_message':'Exception occured'}))

@csrf_exempt
def get_count_of_students(request):
        #if request.method=='GET':
	students_record=models.Student.objects.filter(student_class__teacher__salary__gt='12').aggregate(total_sal=Sum('student_class__teacher__salary'),no_of_students=Count('id'))
	print('##',students_record)
	return HttpResponse(json.dumps({'status':200, 'response_data':students_record}))

def get_counts_of_all(request):
	count_data=models.Subject.objects.annotate(a=Count('subject')).filter(a__gt=1).aggregate(total_duration=Sum('total_duration'),total_teachers=Sum('a'))
	return HttpResponse(json.dumps({'status':200, 'response_data':count_data}))

