from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
#from django.template import loader

from .models import Question

# Create your views here.
def index(request):
  #return HttpResponse("hello,world.")
  latest_question_list = Question.objects.order_by('pub_date')[:5]
  context = {
    "latest_question_list" : latest_question_list,
  }
  return render(request, "polls/index.html", context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
  return HttpResponse("You are looking at the results of question %s." % question_id)

def vote(request, question_id):
  return HttpResponse("You are voting on question %s" % question_id)