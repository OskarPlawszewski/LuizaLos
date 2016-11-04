from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from events.models import Event
from .forms import EventForm
from datetime import datetime

def event_list(request):
    all_events = {}
    today = datetime.today()
    # past_events = Event.objects.filter(end_date__range=["2015-01-01", today]).order_by('published_date')
    # future_events = Event.objects.filter(end_date__range=[today, "2111-01-01"]).order_by('published_date')
    future_events = Event.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # all_events['past_events'] = past_events
    all_events['future_events'] = future_events
    return render(request, 'blog/events_list.html', all_events)


def event_detail(request, pk):
    post = get_object_or_404(Event, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def event_edit(request, pk):
    post = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
