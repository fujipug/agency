from django.shortcuts import render
from main.models import Candidate
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context


def democrat_list(request):
    democrats = Candidate.objects.all().filter(party="Democrat")
    template = get_template('main/democrat_list.html')
    html = template.render(Context({'dems': democrats}))
    return HttpResponse(html)
