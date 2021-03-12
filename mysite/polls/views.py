
from django.shortcuts import get_object_or_404, render
# Create your views here.
import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from django.utils import timezone


# This view lists all the available polls / questions.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:6]


# This view shows the specific poll's polling station with voting options
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# This view shows the specific poll's current voting results
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# This view shows the delete confirmation when a poll is being deleted
class DeleteQuestionView(DeleteView):
    model = Question
    template_name = 'polls/deleteQuestion.html'
    success_url = '/polls/'
    # def get_total_votes(self):
    #     total_votes = 0
    #     for choice in self.choice_set.all:
    #         total_votes += choice.votes
    #     return total_votes


# This view shows a new question / poll creation form
class NewQuestionView(CreateView):
    model = Question
    template_name = 'polls/newQuestion.html'
    fields = ['question_text']
    # success_url = '/polls/'
    # def get_total_votes(self):
    #     total_votes = 0
    #     for choice in self.choice_set.all:
    #         total_votes += choice.votes
    #     return total_votes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["range"] = range(3)
        return context


# This function handles a new question and its choices being posted to database.
def add_new_question(request):
    # extract all form fields data
    new_question_text = request.POST['question_text']
    pub_date = request.POST.get('pub_date')
    pub_time = request.POST.get('pub_time')
    pub_date_time = pub_date + " " + pub_time

    choice_0 = request.POST.getlist('choice')[0]
    choice_1 = request.POST.getlist('choice')[1]
    choice_2 = request.POST.getlist('choice')[2]
    choice_3 = request.POST.getlist('choice')[3]

    date_time_obj = datetime.datetime.strptime(pub_date_time, '%Y-%m-%d %H:%M:%S')

    # persist new question / poll into database, along with choices
    new_question = Question(question_text=new_question_text, pub_date=date_time_obj)
    new_question.save()
    if choice_0:
        new_question.choice_set.create(choice_text=choice_0, votes=0)
    if choice_1:
        new_question.choice_set.create(choice_text=choice_1, votes=0)
    if choice_2:
        new_question.choice_set.create(choice_text=choice_2, votes=0)
    if choice_3:
        new_question.choice_set.create(choice_text=choice_3, votes=0)

    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    return HttpResponseRedirect(reverse('polls:index'))


# This function handles updating database when a vote is submitted for a poll/question.
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
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

