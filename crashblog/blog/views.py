from django.db.models import Q
from django.shortcuts import render, redirect


from .forms import CommentForm
from .models import Post, Category
from django.shortcuts import get_object_or_404



# Create your views here.
def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)    

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

             # Redirect to the same page to avoid resubmission
            return redirect('post_detail', slug=slug)

    else:
        form = CommentForm()

           

    form = CommentForm()
    # Handle form submission
    # Assuming you want to render a template with the post details
    return render(request, 'blog/detail.html', {'post': post, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE).order_by('-created_at')
    
    return render(request, 'blog/category.html', {'category': category, 'posts': posts }) 

def search(request):
    query = request.GET.get('query', '')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query, status=Post.ACTIVE) | Q(intro__icontains=query, status=Post.ACTIVE) | Q(body__icontains=query, status=Post.ACTIVE) | Q(category__title__icontains=query, status=Post.ACTIVE)).distinct()
    else:
        posts = Post.objects.none()
    
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})