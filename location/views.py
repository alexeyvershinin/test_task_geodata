from django.shortcuts import render, redirect
from location.forms import CadastralNumberForm
from rosreestr2coord import Area
from django.contrib import messages
import folium
from location.models import PlotData
from location.utils import get_lst


# Create your views here.
def show_map(request):
    if request.method == 'POST':
        form = CadastralNumberForm(request.POST)
        if form.is_valid():
            area = Area(code=form.cleaned_data['number'])
            if area.code_id:  # проверяем найден ли по запросу участок
                points_list = area.get_coord()  # получаем координаты крайних точек участка
                lst = []
                for i in points_list[0][0]:
                    i[0], i[1] = i[1], i[0]
                    lst.append(i)
                print(points_list)
                # создаем объект с данными полученными из rosreestr2coord
                PlotData.objects.create(
                    number=form.cleaned_data['number'],
                    center_point_x=area.center['x'],
                    center_point_y=area.center['y'],
                    polygon_coordinates=lst
                )
                if len(lst) >= 4:
                    messages.success(request, f"Информация об участке {form.cleaned_data['number']}")
                else:
                    messages.success(request, f"Информация об участке {form.cleaned_data['number']},\n"
                                              f"по данному номеру не удается получить координаты межевания")
            else:
                messages.error(request, 'Проверьте правильность кадастрового номера')
            return redirect('/')
    else:
        form = CadastralNumberForm()

    plot = PlotData.objects.all().last()

    # если объект найден
    if plot:
        center_point = [plot.center_point_y, plot.center_point_x]  # координаты центральной точки участка
        # на основе координат крайних точек участка формируем список, для заполнения полигона
        m = folium.Map(location=center_point, zoom_start=20)
        folium.Marker(location=center_point, icon=folium.Icon(color='green'), popup=plot.number).add_to(
            m)  # добавляем маркер
        polygon = get_lst(plot.polygon_coordinates)  # преобразовываем строку в список со значениями float
        folium.Polygon(locations=polygon, fill_color="blue", weight=2.5, opacity=1).add_to(m)  # добавляем полигон

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
