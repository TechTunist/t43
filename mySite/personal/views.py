from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    # return HttpResponse("This is a test of routing")
    return render(request, 'home.html')


def testURL(request):

    return render(request, 'testURL.html')