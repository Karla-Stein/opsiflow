from django.shortcuts import render


def index(request):
    """
    A view to return th eindex page
    """
    return render(
        request,
        'home/index.html'
    )
