from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    
    return render(request, 'core/frontpage.html', {'posts': posts}) 

def about (request):
    return render(request, 'core/about.html' )

def robot_txt (request):
    text = [
        'User-agent: *',
        'Disallow: /admin/',
    ]
    return HttpResponse('\n'.join(text), content_type='text/plain')