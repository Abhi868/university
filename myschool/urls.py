from django.urls import path
from myschool import views
urlpatterns = [
    path('' , views.get_classroom_data.as_view(),name='get_classroom_data'),
]

