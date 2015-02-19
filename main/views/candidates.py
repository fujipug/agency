from django.shortcuts import render

def index(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    template = get_template('main/candidates_base.html')
    html = template.render(Context({'c' : candidate}))
    return HttpResponse(html)
