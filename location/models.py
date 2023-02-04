from django.db import models


# Create your models here.
class PlotData(models.Model):
    number = models.CharField(max_length=200, null=True)  # кадастровый номер
    center_point_x = models.FloatField(null=True)  # координаты центральной метки участка широта
    center_point_y = models.FloatField(null=True)  # координаты центральной метки участка долгота
    # координаты крайних точек участка
    polygon_coordinates = models.CharField(max_length=200, null=True)  # координаты полигона
