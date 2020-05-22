from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = 'polls/list.html'
    context_object_name = 'questions'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'question'

class QuestionResultView(DetailView):
    model = Question
    template_name = 'polls/result.html'
    context_object_name = 'question'
    pk_url_kwarg = 'question_id'

def calcvote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
       selected_choice = q.choice_set.get(pk=request.POST["choice"])
    except:
        return HttpResponse("No choice selected")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #data = {'question': q}
        #return render(request, 'polls/detail.html', data)
        return HttpResponseRedirect(reverse('polls:result', args=(q.id,)))

