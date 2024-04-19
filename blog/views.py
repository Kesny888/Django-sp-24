from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
#this adds a post list function the defer to the post list html page. We respond to a request, send the brower to aassociate html page, and pass any date on to it

def post_list(request):
    #this is where you are going to put your quries (for the most part)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' :posts})