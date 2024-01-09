from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.subject_chapter_form, name='subject_chapter_form'),
    path('create_question_set/<int:form_id>/', views.question_set, name='question_set'),
    path('add_questions/<int:question_set_id>/', views.add_questions, name='add_questions'),
    path('add_topics/<int:form_id>/', views.add_topics, name='add_topics'),  
    path('select/', views.select_group_subject_chapter, name='select_group_subject_chapter'),
    path('subject-chapter/<int:form_id>/', views.list_question_sets, name='list_question_sets'),
    path('question-set/<int:question_set_id>/', views.list_questions, name='list_questions'),
  
]
