from django.shortcuts import render
import pandas as pd
from django_pandas.io import read_frame
from firstUI.models import Tempcolor

df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
# could not change time at 9:21
# could change time at 10:15
# could change time at 10:00
def indexPage(request):

    confirmedGlobal= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    totalCount = confirmedGlobal[confirmedGlobal.columns[-1]].sum()
    barPlotData = confirmedGlobal[['Country/Region',confirmedGlobal.columns[-1]]].groupby('Country/Region').sum().sort_values(by='9/16/21',ascending=False)
    barPlotData = barPlotData.reset_index()
    barPlotData.columns = ['Country/Region','values']
    barPlotData = barPlotData.sort_values(by='values',ascending=False)
    barPlotVals = barPlotData['values'].values.tolist()
    countryNames = barPlotData['Country/Region'].values.tolist()
    dataForMap = mapDataCal(barPlotData,countryNames)
    showMap = 'True'
    context = {'totalCount':totalCount,'countryNames':countryNames,'barPlotVals':barPlotVals, 'dataForMap':dataForMap, 'showMap': showMap}
    return render(request,'index.html',context)
# Create your views here.
# test comment

'''
def indexPage(request):

    confirmedGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    totalCount = confirmedGlobal[confirmedGlobal.columns[-1]].sum()
    barPlotData = confirmedGlobal[['Country/Region',confirmedGlobal.columns[-1]]].groupby('Country/Region').sum().sort_values(by='7/27/21',ascending=False)
    barPlotData = barPlotData.reset_index()
    barPlotData.columns = ['Country/Region','values']
    barPlotData = barPlotData.sort_values(by='values',ascending=False)
    barPlotVals = barPlotData['values'].values.tolist()
    countryNames = barPlotData['Country/Region'].values.tolist()
    dataForMap = mapDataCal(barPlotData,countryNames)
    showMap = 'True'
    context = {'totalCount':totalCount,'countryNames':countryNames,'barPlotVals':barPlotVals, 'dataForMap':dataForMap, 'showMap': showMap}
    return render(request,'index.html',context)

'''

def mapDataCal(barPlotData,countryNames): 
    dataForMap=[]
    df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
    for i in countryNames:
        try:
            tempdf=df3[df3['name']==i]
            temp={}
            temp["code3"]=list(tempdf['code3'].values)[0]
            temp["name"]=i
            temp["value"]=barPlotData[barPlotData['Country/Region']==i]['values'].sum()
            temp["code"]=list(tempdf['code'].values)[0]
            dataForMap.append(temp)
        except:
            pass
    return dataForMap

def indiCountryData(request):
    countryNameSe=request.POST.get('countryName')
    confirmedGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    #totalCount = confirmedGlobal[confirmedGlobal.columns[-1]].sum()
    qs = Tempcolor.objects.all()
    totalCount = read_frame(qs)
    totalCount = totalCount.columns[-1]
    barPlotData = confirmedGlobal[['Country/Region',confirmedGlobal.columns[-1]]].groupby('Country/Region').sum().sort_values(by='9/16/21',ascending=False)
    barPlotData = barPlotData.reset_index()
    barPlotData.columns = ['Country/Region','values'] 
    barPlotData = barPlotData.sort_values(by='values',ascending=False)
    barPlotVals = barPlotData['values'].values.tolist()
    countryNames = barPlotData['Country/Region'].values.tolist()
    showMap = 'False'

    import psycopg2
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Darkknight17")
    cur = conn.cursor()
    x = """DELETE from jcst.stagecolor /* test */"""
    cur.execute(x)
    conn.commit()
    conn.close()

    

 
    countryDataSpe=pd.DataFrame(confirmedGlobal[confirmedGlobal['Country/Region']==countryNameSe][confirmedGlobal.columns[4:-1]].sum().reset_index())
    countryDataSpe.columns=['country','values']
    countryDataSpe['lagVal']=countryDataSpe['values'].shift(1).fillna(0)
    countryDataSpe['incrementalVal']=countryDataSpe['values']-countryDataSpe['lagVal']
    countryDataSpe['rollingMean']=countryDataSpe['incrementalVal'].rolling(window=4).mean()
    countryDataSpe=countryDataSpe.fillna(0)
    datasetsForLine=[{'label':'Daily Cumulated Data','data':countryDataSpe['values'].values.tolist()},
                       {'label':'Rolling Mean 4 days','data':countryDataSpe['rollingMean'].values.tolist()}]

    axisvalues=countryDataSpe.index.tolist()
    context = {'axisvalues':axisvalues, 'countryName':countryNameSe, 'totalCount':totalCount,'countryNames':countryNames,'barPlotVals':barPlotVals, 'showMap': showMap, 'datasetsForLine':datasetsForLine}
    return render(request,'index.html',context)

