from django.urls import path
from myschool import views
urlpatterns = [
    path('' , views.get_classroom_data.as_view(),name='get_classroom_data'),
    path('search_for/', views.get_list_of_students, name='search_for_teacher'),
    path('get_count_of_students/' , views.get_count_of_students ,name='get_count_of_students'),
    path('get_counts_of_all/' ,views.get_counts_of_all,name='get_counts_of_all')
]

