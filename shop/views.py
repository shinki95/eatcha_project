from django.shortcuts import get_object_or_404, render
from .models import Post
# Create your views here.

def post_list(request):
    qs = Post.objects.all()
    return render(request, 'post_list.html', {'qs':qs })

def post_detail(request, id):
    tag = request.GET.get('tag','')
    post = get_object_or_404(Post, id=id)
    next_post_list = Post.objects.filter(id__gt=post.id).order_by('id')
    prev_post_list = Post.objects.filter(id__lt=post.id).order_by('-id')

    if tag:
        next_post_list = next_post_list.filter(tag_set__name__iexact=tag)
        prev_post_list = prev_post_list.fitler(tag_set__name__iexact=tag)

    return render(request, 'post_detail.html', {
        'post': post,
        'next_post': next_post_list.first(),
        'prev_post': prev_post_list.first(),
        'tag': tag,
    })


