from bokeh.plotting import figure, show, save
from bokeh.models import HoverTool, ColumnDataSource
from datetime import datetime
# from script import df

import pandas

df = pandas.read_csv("Times.csv", parse_dates=['Start', 'End'])

df["Start_string"] = df["Start"].dt.strftime("%Y-%m%d %H-%M-%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m%d %H-%M-%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=100, width=500,
           sizing_mode="scale_width", title='Motion Graph')
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1


hover = HoverTool(
    tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(
    source=cds,
    left="Start",
    right="End",
    top=1, bottom=0, color='blue')

# p.quad(
#     left=[datetime.fromisoformat(i) for i in df["Start"].values],
#     right=[datetime.fromisoformat(i) for i in df["End"].values],
#     top=1, bottom=0, color='blue')

save(p)

show(p)
