#!/usr/bin/python
#-*- codong: utf-8 -*- 
import requests
import json
from pandas import DataFrame
from coincheck import market, order
import matplotlib.pyplot as plt 
from time import sleep
from datetime import datetime 
from sender import Line

ma = market.Market()

URL = "https://coincheck.com/api/rate/"
#params = {"order_type":"sell", "pair": "btc_jpy", "amount": 0.1}
#requests.get(URL, params=params).json()

coins = {"BTC":"btc_jpy", "XEM": "xem_jpy", "XRP": "xrp_jpy"}
wait = 60
xem = []
xrp = []
btc = []
time = []

if __name__ == '__main__':
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        sec = now.second
        time.append(str(hour) + ":" + str(minute) + ":" + str(sec))
        message = ""
        print (str(hour) + ":" + str(minute) + ":" + str(sec))

        for key,item in coins.items():
            coincheck = requests.get(URL+item).json()
            if key == "XEM":
                xem.append(coincheck["rate"])
            if key == "XRP":
                xrp.append(coincheck["rate"])
            if key == "BTC":
                btc.append(coincheck["rate"])
                
               # if(float(coincheck["rate"]) > 155.0):
               #     #Line().sender("XRP over 155 yen" + coincheck["rate"])
               #     exit()
               # 
               # elif(float(coincheck["rate"]) < 145.0):
               #     #Line().sender("XRP under 145 yen" + coincheck["rate"])
               #     exit()

            message = "%-4s : %-10s" % (key, coincheck["rate"])
            print message
        #plt.plot(xrange(len(xrp)),xrp)
        #plt.draw()
        sleep(wait)
        

