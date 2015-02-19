from django.shortcuts import render
from main.forms import FreeStuffForm
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.http import HttpResponse
from main.models import Candidate
from django.template import Context


def free_stuff_form(request):
    if request.method == 'GET':
        form = FreeStuffForm()
    else:
        # A POST request: Handle Form Upload
        form = FreeStuffForm(request.POST) # Bind data from request.POST 
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            #post = PostForm.objects.create(content=content, created_at=created_at)
            form.save()
            return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))
 
    return render(request, 'main/free_stuff_form.html', {
        'form': form, })


    #When making changes to class 
    #!.) python manage.py makemigrations main
    #2.) python manage.py migrate
