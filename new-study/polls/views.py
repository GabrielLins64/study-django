from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.db.models import F
from django.views import generic
from polls.models import Question, Choice


class IndexView(generic.ListView):
    """The generic ListView uses by default the template
    name "<app_name>/<model_name>_list.html". Also, the
    default context name is <model>_list."""
    # template_name = 'polls/index.html' # overrides "polls/question_list.html"
    # context_object_name = 'latest_question_list' # overrides "question_list" default ctx name
    # model = Question # Not required, since get_queryset returns Question model

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.localtime()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """The generic DetailView uses by default the template
    name "<app_name>/<model_name>_detail.html". Also, the
    default context name is <model>."""
    model = Question
    # template_name = 'polls/detail.html' 

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.localtime())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html' # overrides "<app_name>/<model_name>_detail.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        selected_choice.votes = F('votes') + 1 # Avoid race conditions because F
                                               # expressions forces the database
                                               # to perform the queries.
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))