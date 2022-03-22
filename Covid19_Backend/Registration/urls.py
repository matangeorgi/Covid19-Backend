from django.urls import path
from . import views

urlpatterns = [
    path('summary/getData/',views.getDataFilter),
    path('summary/getData',views.getData),
    path('register/',views.addData),
    path('summary/exportExcel',views.ExportExcel)
]