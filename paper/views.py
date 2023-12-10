from django.shortcuts import render, get_object_or_404, redirect
from .models import Paper,PaperTag,Publication,FieldResearch,JournalPublication,ConferencePublication,Author
from account.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView



# Create your views here.



# region function base
def paper_list(request):
    papers = Paper.objects.all().order_by('-citation')
    number_of_papers= papers.count()
    average_citations=papers.aggregate(Avg("citation"))
    return render(request, 'paper/paper_list.html', {
        'paper' : papers,
        'sum_of_papers':number_of_papers,
        'average_citations':average_citations
    })
def paper_detail(request, slug):
    # paper = Paper.objects.get(id=paper_id)
    paper= get_object_or_404(Paper, slug=slug)
    return render(request, 'paper/paper_detail.html', {'paper' : paper})
#endregion

#region class base view

class PaperListView(ListView):
    template_name = 'paper/paper_list.html'
    model = Paper
    context_object_name = 'paper'


class PaperDetailView(DetailView):
    template_name = 'paper/paper_detail.html'
    model = Paper

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_paper = self.object
        request = self.request
        favorite_paper_id = request.session.get("paper_favorite")
        context['is_favorite'] = favorite_paper_id == str(loaded_paper.id)
        return context


class AddPaperFavorite(View):
        def post(self, request):
            paper_id = request.POST["paper_id"]
            paper = Paper.objects.get(pk=paper_id)
            request.session["paper_favorite"] = paper_id
            return redirect(paper.get_absolute_url())

#endregion

