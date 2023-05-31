from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Question, Answer, User
from .forms import QuestionForm


# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {
        'question_list': question_list
    }
    return render(request, 'questionnaire/index.html', context)

def question(request, question_id):
    form = QuestionForm()
    cur = connection.cursor()
    # exhibit 2 : SQL injection
    cur.execute(f'SELECT question_text FROM questionnaire_question WHERE ID={question_id}')
    question = cur.fetchone()[0]
    #secure:
    #question_item = get_object_or_404(Question, pk=question_id)
    #question = question_item.question_text
    context = {
        'question' : question,
        'question_id': question_id,
        'form' : form
    }
    return render(request, 'questionnaire/question.html', context)

def answers(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        answers = get_list_or_404(Answer, question=question)
    except:
        answers = []
    context = {
        'question' : question,
        'answers' : answers
    }
    return render(request, 'questionnaire/answers.html', context)

#@csrf_protect
@csrf_exempt
def answer(request, question_id):
    if request.method == 'POST':
        user_id = 0
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                submitter = User.objects.get(pk=user_id)
            except:
                submitter = User.objects.create(name="Bogusperson", password="ding")
            question = Question.objects.get(pk=question_id)
            ans = Answer.objects.create(submitter=submitter, question=question, answer=form.cleaned_data["answer"])
            return answers(request, question_id)

#secure :
#@login_required
def delete_answer(request, question_id, answer_id):
    # exhibit 1 = lack of authentication for this operation
    answer = Answer.objects.get(pk=answer_id)
    answer.delete()
    return index(request)
