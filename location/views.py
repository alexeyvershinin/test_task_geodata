from django.shortcuts import render
from location.forms import CadastralNumberForm
import folium


# Create your views here.
def show_map(request):
    if request.method == 'POST':
        form = CadastralNumberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['number'])
    else:
        form = CadastralNumberForm()
    # карта
    m = folium.Map(location=[64.6863136, 97.7453061], zoom_start=3)
    m = m._repr_html_()

    context = {
        'form': form,
        'm': m
    }
    return render(request, 'location/index.html', context)
