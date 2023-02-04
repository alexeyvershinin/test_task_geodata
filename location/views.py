from django.shortcuts import render, redirect
from location.forms import CadastralNumberForm
from rosreestr2coord import Area
from django.contrib import messages
import folium

from location.models import PlotData


# Create your views here.
def show_map(request):
    if request.method == 'POST':
        form = CadastralNumberForm(request.POST)
        if form.is_valid():
            area = Area(code=form.cleaned_data['number'])
            if area.code_id:  # проверяем найден ли по запросу участок
                # создаем объект с данными полученными из rosreestr2coord
                PlotData.objects.create(
                    number=form.cleaned_data['number'],
                    center_point_x=area.center['x'],
                    center_point_y=area.center['y']
                )
                messages.success(request, f"Информация об участке {form.cleaned_data['number']}")
            else:
                messages.error(request, 'Проверьте правильность кадастрового номера')
            return redirect('/')
    else:
        form = CadastralNumberForm()

    plot = PlotData.objects.all().last()

    # если объект найден
    if plot:
        center_point = [plot.center_point_y, plot.center_point_x]  # координаты центральной точки участка
        m = folium.Map(location=center_point, zoom_start=20)
        folium.Marker(location=center_point, icon=folium.Icon(color='green'), popup=plot.number).add_to(
            m)  # добавляем маркер

    # если в базе нет объектов, отображаем карту с фиксированными параметрами
    else:
        m = folium.Map(location=[64.6863136, 97.7453061], zoom_start=3)
    m = m._repr_html_()

    PlotData.objects.all().delete()  # удаляем все объекты из базы данных
    context = {
        'form': form,
        'm': m
    }
    return render(request, 'location/index.html', context)
