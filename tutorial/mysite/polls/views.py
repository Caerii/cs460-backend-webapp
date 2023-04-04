from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader #html template loader
from django.shortcuts import get_object_or_404,render # html render function
from django.urls import reverse
from django.views import generic


from .models import Question
from .models import Choice

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = { 
#         'latest_question_list': latest_question_list, # equating list to the variable in the template
#     }
#     return render(request, 'index.html',context)

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# def details(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request ,'detail.html', {'question': question})
#     question=get_object_or_404(Question, pk= question_id)
#     return render(request, 'details.html', {'question' : question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'details.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
