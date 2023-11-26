from django.shortcuts import render
from .models import Paper,PaperTag,Publication,FieldResearch,JournalPublication,ConferencePublication,Author
from account.models import User
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render , get_object_or_404
from django.db.models import Avg

# Create your views here.

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