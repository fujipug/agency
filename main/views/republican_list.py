from django.shortcuts import render
from main.models import Candidate
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context


def republican_list(request):
    republicans = Candidate.objects.all().filter(party="Republican")
    template = get_template('main/republican_list.html')
    html = template.render(Context({'reps': republicans}))
    return HttpResponse(html)
