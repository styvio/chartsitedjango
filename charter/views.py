from django.shortcuts import render
import requests
import json
import random

def chartPage(request, *args, **kwargs):
    context = {}


    # #  search bar logic  # #
    stockList = ["MSFT", "FB", "AAPL", "AMZN", "NFLX", "GOOG", "BABA", "NVDA", "TSLA",
                "ZM", "MELI", "JMIA", "SHW", "HD", "TDOC", "DOCU", "XPO", "FRTA", "MDB"
                "TGT", "WMT", "ACI", "ENPH", "JKS", "RUN", "PLUG", "BE", "NET", "DDOG", 
                "FSLY", "OKTA", "AYX", "AZN", "AMGN", "PFE", "CSCO", "TSM", "PINS", "WM", "MMM",
                "DE", "CAT", "VZ", "TMUS", "T", "NVAX", "REGN", "PYPL", "SQ", "JPM"]

    randomStock = (random.choice(stockList))

    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
    if(search_query is None):
        search_query = randomStock
    tickerText = search_query.upper()

    try:
        out = (requests.get("https://www.styvio.com/api/" + str(tickerText))).json()
    except:
        out = (requests.get("https://www.styvio.com/api/" + str(randomStock))).json()
    # # end search bar logic  # #    


    # #  API logic  # #
    ticker = out['ticker']
    currentPrice = out['currentPrice']

    context['ticker'] = ticker
    context['currentPrice'] = currentPrice

    hist1 = out['dailyStockValues']
    hist15 = out['weeklyStockValuesIntraday']
    hist51 = out['weeklyStockValuesDaily']
    hist530 = out['weeklyStockValuesHalfHours']
    histMonth11 = out['monthlyStockValues']
    histYear = out['yearlyStockValues']

    context['hist1'] = hist1
    context['hist15'] = hist15
    context['hist51'] = hist51
    context['hist530'] = hist530
    context['histMonth11'] = histMonth11
    context['histYear'] = histYear

    context['hist1Test'] = [10,30,20,40]
    context['hist15Test'] = [10,30,20,40,60,50]
    context['hist51Test'] = [10,30,20,40,60,70,80,90]
    context['hist530Test'] = [10,30,20,40,60,70,80,90,110,120,140,110,150]
    context['histMonth11Test'] = [10,30,20,40,60,70,80,90,110,120,140,110,150,200,160]
    context['histYearTest'] = [10,30,20,40,60,70,80,90,110,120,140,110,150,200,160,180,200,170,120,220]
    # #  end API logic  # #

    # #  load the page!  # #
    return render(request, 'chartPage.html', context)
    # #  good work bois  # #