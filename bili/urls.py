from django.urls import path

from . import views

app_name = 'bili'

urlpatterns = [
    path('', views.index, name='index'),
    path('chapters', views.chapters, name='chapters'),
    path('new_chapter', views.new_chapter, name='new_chapter'),
    path('<int:chapter_id>/', views.chapter, name='chapter'),
    path('chapters/edit_chapter/<int:chapter_id>/', views.edit_chapter, name="edit_chapter"),
    path('chapters/del_chapter/<int:chapter_id>/', views.del_chapter, name="del_chapter"),
    
    path('chapters/new_entry/<int:chapter_id>/', views.new_entry, name="new_entry"),
    path('chapters/edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry"),
    path('chapters/del_entry/<int:entry_id>/', views.del_entry, name="del_entry"),
    
    path('chapters/new_exercise/<int:chapter_id>/<int:entry_id>/', views.new_exercise, name="new_exercise"),
    path('chapters/edit_exercise/<int:exercise_id>/', views.edit_exercise, name="edit_exercise"),
    path('chapters/<int:exercise_id>/', views.exercise, name='exercise'),
    path('chapters/<int:exercise_id>/html/', views.exercise_html, name='exercise_html'),
    path('chapters/del_exercise/<int:exercise_id>/', views.del_exercise, name="del_exercise"),
    

    path('goto', views.goto, name='goto'),
]