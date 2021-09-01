import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
count_crs = data.groupby(['Course Name'])['Rating'].count()

chart_def = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Number of Rating for each Course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", 
    classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis",
    classes='text-h6 q-pa-sm text-weight-medium')

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(count_crs.index)
    
    hc_data = [{"name": v1, "y": v2} for v1,v2 in zip(count_crs.index,count_crs)]
    
    hc.options.series[0].data = hc_data

    return wp

jp.justpy(app)