from django.shortcuts import redirect, render
from .forms import TweetForm
from .models import Tweet


def home(request):

    if request.method == 'POST':
        tweet_form = TweetForm(request.POST or None)

        if tweet_form.is_valid():
            tweet_form.save()
            return redirect('tweets_home')
    else:
        tweet_form = TweetForm()
        tweets = Tweet.objects.all()
        context = {
            'tweet_form': tweet_form,
            'tweets': tweets
        }
        return render(request, 'tweets/home.html', context)
