from django.db import models


# Create your models here.
class PlotData(models.Model):
    number = models.CharField(max_length=200, null=True)  # кадастровый номер
    center_point_x = models.FloatField(null=True)  # координаты центральной метки участка широта
    center_point_y = models.FloatField(null=True)  # координаты центральной метки участка долгота
    # координаты крайних точек участка
    point_a_x = models.FloatField(null=True)
    point_a_y = models.FloatField(null=True)
    point_b_x = models.FloatField(null=True)
    point_b_y = models.FloatField(null=True)
    point_c_x = models.FloatField(null=True)
    point_c_y = models.FloatField(null=True)
    point_d_x = models.FloatField(null=True)
    point_d_y = models.FloatField(null=True)
