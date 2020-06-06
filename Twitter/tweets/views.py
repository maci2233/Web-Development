from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tweet


def home(request, *args, **kwargs):
    return render(request, 'pages/home.html', status=200)

#REST API VIEW
def tweet_list(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    tweets_list = [{'id': t.id, 'content': t.content} for t in tweets]
    data = {
        'isUser': False,
        'response': tweets_list
    }
    return JsonResponse(data)

#REST API VIEW
def tweet_detail(request, id, *args, **kwargs):
    data = {
        'id': tweet.id,
    }
    try:
        tweet = Tweet.objects.get(id=id)
        data['content'] = tweet.content
        status = 200
    except:
        data['message'] = "Not Found"
        status = 404
    return JsonResponse(data, status=status)
