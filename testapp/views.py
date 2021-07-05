from django.shortcuts import render
import requests
from django.http import HttpResponse
from BRM import settings

def yt(request):
    search_url="https://www.googleapis.com/youtube/v3/search"
    params={
        'part':'snippet',
        'q':'learn python',
        'key':settings.YOUTUBE_DATA_API_KEY,
        'type':'video'
    }
    r=requests.get(search_url,params=params)
    title=r.json()['items'][2]['snippet']['title']
    video_id=r.json()['items'][0]['id']['videoId']
    s="<a href='https://www.youtube.com/watch?v="+video_id+"'>'"+title+"</a>"
    return HttpResponse(s)
