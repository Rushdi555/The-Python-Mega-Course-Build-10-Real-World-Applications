import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_count_crs = data.groupby(['Month', 'Course Name'])['Rating'].count().unstack()

chart_def = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    // Make sure connected countries have similar colors

    title: {
        floating: true,
        align: 'left',
        text: 'Number of Rating for each Course by Month'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Source: reviews.csv file'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 0,
                xAxis: 0,
                y: 0,
                yAxis: 0
            },
            text: 'Most<br>Courses<br>Launched'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", 
    classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis",
    classes='text-h6 q-pa-sm text-weight-medium')

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(month_count_crs.index)
    
    hc_data = [{"name": v1, "data": [v2 for v2 in month_count_crs[v1]]} for v1 in month_count_crs.columns]
    
    hc.options.series = hc_data

    return wp

jp.justpy(app)