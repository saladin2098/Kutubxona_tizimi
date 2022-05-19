from  django.contrib import admin
from django.urls import path
from app1.views import *
from university.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', all_students),
    path('data/', all_data),
    path('mualliflar/', all_mualliflar),
    path('sub/', all_fanlar),
    path('yonalish/', all_yonalishlar),
    path('ustozlar/', all_ustozlar),
    path('student/<int:pk>/', student_och),
    path('muallif/<int:pk>/', muallif_och),
    path('ustoz/<int:pk>/', ustoz_och),
    path('yon/<int:pk>/', yonalish_och),
    path('recordlar/', all_recordlar),
    path('student/<int:pk>/edit/' , student_edit),
    path('muallif/<int:pk>/edit/' , muallif_edit),
    path('kitob/<int:pk>/edit/' , kitob_edit),
    path('yon/<int:pk>/edit/' , yonalish_edit),
    path('ustoz/<int:pk>/edit/', ustoz_edit),
]
