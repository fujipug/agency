from django.shortcuts import render
from main.models import Candidate
from django.template import Context


def index(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    context = {'c': candidate}
    return render(request, 'main/candidates_base.html', context)
   # template = get_template('main/candidates_base.html')
   # html = template.render(Context({'c' : candidate}))
   # return HttpResponse(html)
