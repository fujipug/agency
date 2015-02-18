from django.shortcuts import render
from main.forms import PostFormForm
from django.http import HttpResponseRedirect


def post_form_upload(request):
    if request.method == 'GET':
        form = PostFormForm()
    else:
        # A POST request: Handle Form Upload
        form = PostFormForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            #post = PostForm.objects.create(content=content, created_at=created_at)
            form.save()
            return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))
 
    return render(request, 'main/post_form_upload.html', {
        'form': form, })
