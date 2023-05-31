from django.urls import path
from . import views

app_name = 'questionnaire'
urlpatterns = [
    # ex: /questionnaire/
    path('', views.index, name='index'),
    # ex: /questionnaire/5/
    path('<int:question_id>/', views.question, name='question'),
    # ex: /questionnaire/5/answer
    path('<int:question_id>/answer/', views.answer, name='answer'),
    # ex: /questionnaire/5/answers
    path('<int:question_id>/answers/', views.answers, name='answers'),
    # ex: /questionnaire/5/answers/2/delete
    path('<int:question_id>/answers/<int:answer_id>/delete', views.delete_answer, name='delete_answer'),
]
