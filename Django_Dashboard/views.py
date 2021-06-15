import numpy as np
from .chart import chart_func
from bokeh.embed import components
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin
from django.shortcuts import render


def index(request):
    chart = chart_func()
    script,div = components(chart)
    return render(request, 'index.html', {'div': div, 'script':script})
