from django.shortcuts import render

# Create your views here.
def show_map(request):
    return render(request, 'location/index.html')
