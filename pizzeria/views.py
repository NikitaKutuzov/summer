from django.shortcuts import render


def main(request):

    return render(request, "main.html")

def My_map(request):

    return render(request, "My_map.html")