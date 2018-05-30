from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def viewPapers(request):
    papers = Paper.objects.filter(owner=request.user)
    if request.user.is_authenticated():
        return render(request, 'papers/list_papers.html', {'papers': papers})
    else:
        return redirect('/login')

def viewPaper(request, paper_id):
    if request.user.is_authenticated():
        paper = Paper.objects.get(id=paper_id)
        if (paper.owner == request.user):
            return render(request, 'HTML FILE', {'papers': papers})
        else:
            return redirect('/login')
    else:
        return redirect('/login')

def editPaper(request, paper_id):
    if request.user.is_authenticated():
        paper = Paper.objects.get(id=paper_id)
        if (paper.owner == request.user):
            return render(request, 'HTML FILE', {'papers': papers})
        else:
            return redirect('/login')
    else:
        return redirect('/login')

def createPaper(request):
    if request.user.is_authenticated():
        if (request.method == 'POST'):
            form = NewPaperForm(request.POST)
            if form.is_valid():
                paper = form.save(commit=False)
                paper.owner = request.user
                paper.save()

                return redirect('/papers')
        else:
            form = NewPaperForm()
        # Filter this by single slot events in the future
        return render(request, 'papers/create_paper.html', {'form': form})

    else:
        return redirect('/login')

def addSection(request, paper_id):
    if request.user.is_authenticated():
        paper = Paper.objects.get(id=paper_id)
        if (paper.owner == request.user):
            return render(request, 'HTML FILE', {'papers': papers})
        else:
            return redirect('/login')
    else:
        return redirect('/login')

def editSection(request, section_id):
    if request.user.is_authenticated():
        section = Section.objects.get(id=section_id)
        if (seciton.parentPaper.owner == request.user):
            return render(request, 'HTML FILE', {'section': section})
        else:
            return redirect('/login')
    else:
        return redirect('/login')
