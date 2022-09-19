from django.urls import path,include

from . import views

from django.urls import re_path   
from django.views import static   
from django.conf import settings

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    re_path(r"^static/(?P<path>.*)$",static.serve,{'document_root':settings.STATIC_ROOT},name='static'),
]
