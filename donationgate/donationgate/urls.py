from django.contrib import admin
from django.urls import path
from donation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="homepage"),
    path('detailspage/',views.detailspage,name="detailspage"),
    path('donatepage/',views.donatepage,name="donatepage"),
    path('success/', views.successpage, name='successpage'),
    path('failure/', views.failurepage, name='failurepage'),
]
