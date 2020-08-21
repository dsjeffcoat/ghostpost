from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostapp.models import GhostPost
from ghostapp.forms import GhostForm
# Create your views here.


def index(request):
    posts_list = GhostPost.objects.order_by("-time_submitted")
    return render(request, 'index.html', {'posts': posts_list})


def votes_view(request):
    post_set = GhostPost.objects.all()
    sorted_posts = sorted(
        post_set, key=lambda p: p.total_score(), reverse=True)
    return render(request, 'votes.html', {'voted_posts': sorted_posts})


def upvote_view(request, post_id):
    post = GhostPost.objects.get(id=post_id)
    post.upvote += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def downvote_view(request, post_id):
    post = GhostPost.objects.get(id=post_id)
    post.downvote += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def boasts_view(request):
    all_boasts = GhostPost.objects.filter(
        is_boast=True).order_by('-time_submitted')
    return render(request, 'boasts.html', {'boasts': all_boasts})


def roasts_view(request):
    all_roasts = GhostPost.objects.filter(
        is_boast=False).order_by('-time_submitted')
    return render(request, 'roasts.html', {'roasts': all_roasts})


def createpost_view(request):
    if request.method == 'POST':
        form = GhostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPost.objects.create(
                post=data.get('post'),
                is_boast=data.get('is_boast')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = GhostForm()
    return render(request, 'generic_form.html', {'form': form})


def deletepost_view(request):
    pass
