from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot/')
def plot():
    from pandas_datareader import data
    from datetime import datetime
    from bokeh.plotting import figure, show
    from bokeh.embed import components
    from bokeh.resources import CDN
    from math import pi

    start = datetime(2021,2,1)
    end = datetime(2021,6,10)

    df = data.DataReader(name="AAPL", data_source="yahoo", start=start, end=end)

    p = figure(title='Stcok Market Apple', x_axis_type='datetime', x_axis_label='Dates', y_axis_label='Amount',
            sizing_mode="scale_width", height=150)
    p.xaxis.major_label_orientation = pi/4
    p.grid.grid_line_alpha=0.3 

    inc = df.Close > df.Open
    dec = df.Open > df.Close
    w = 12*60*60*1000 # half day in ms

    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.vbar(df.index[inc], w, df.Open[inc], df.Close[inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(df.index[dec], w, df.Open[dec], df.Close[dec], fill_color="#F2583E", line_color="black")

    script1 , div1 = components(p)
    cdn_js = CDN.js_files
    return render_template('plot.html', script1=script1, div1=div1, cdn_js=cdn_js[0])

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
 