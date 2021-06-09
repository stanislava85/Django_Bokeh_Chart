import numpy as np

from bokeh.embed import components
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin
from django.shortcuts import render


def index(request):
    n = 50000
    x = np.random.standard_normal(n)
    y = np.random.standard_normal(n)
    bins = hexbin(x, y, 0.3)
    p = figure(title="", tools="wheel_zoom,pan,reset",
               match_aspect=True, background_fill_color="#fff", 
               sizing_mode="scale_both")
    p.grid.visible= False
    p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
               fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))
    script, div = components(p)

    return render(request, 'index.html', {'div': div, 'script':script})
