from django.shortcuts import render
from django.http import HttpResponse
from votinghome.models import Vote
def homepage(request):
    if request.method == 'POST':
        vote=Vote()
        candidate= request.POST.get('candidate')
        vote.candidate=candidate
        Vote.objects.get(pk=candidate)
        vote.save()
            # You can perform additional logic here if needed
        return HttpResponse(f'Vote submitted Successfully.')
    return render(request,'homepage.html',{})