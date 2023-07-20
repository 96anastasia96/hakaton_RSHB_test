from django.shortcuts import render


def start_screen(request):
    return render(request, 'start_screen.html')