#Network Data
import requests
response = requests.get("https://bitaps.com/api/fee")
txfee = response.text
txfeeraw = txfee[8:10]
print("The Bitcoin Low Network Transaction fee is... " + txfeeraw)

import requests
response = requests.get("https://bitaps.com/api/txrate")
txratedata = response.text
txratedataraw = txratedata[12:16]
print("Transactions Per Second... " + txratedataraw)


#BTC Price Data 1
import requests
response = requests.get("https://bitaps.com/api/ticker/average")
pricedata = response.text
fp = pricedata[119:123]
print(fp)

#rename this for time inbetween price updates 
#measured in seconds
import time
time.sleep(30)

#BTC Price Data 2
import requests
response = requests.get("https://bitaps.com/api/ticker/average")
pricedata = response.text
lastprice = pricedata[119:123]
print(lastprice)

#spread creat class for avgs over time
af = int(fp)
b = int(lastprice)

#BULL vs BEAR Price Spread 1
def market1(af,b):
    if af < b:
        return "Bull"
    if af > b:
        return "Bear"

x = market1(af,b)

print(x)

#BTC Price Data 3
import requests
response = requests.get("https://bitaps.com/api/ticker/average")
pricedata = response.text
firstprice = pricedata[119:123]
print(firstprice)

#rename this for time inbetween price updates 
#measured in seconds
import time
time.sleep(30)

#BTC Price Data 4
import requests
response = requests.get("https://bitaps.com/api/ticker/average")
pricedata = response.text
lastprice = pricedata[119:123]
print(lastprice)

a = int(firstprice)
b = int(lastprice)

#BULL vs BEAR Price Spread 2
def market2(a,b):
    if a < b:
        return "Bull"
    if a > b:
        return "Bear"

y = market2(a,b)

print(y)

#BTC Price Data 5
import requests
response = requests.get("https://bitaps.com/api/ticker/average")
pricedata = response.text
firstprice = pricedata[119:123]
print(firstprice)

#rename this for time inbetween price updates 
#measured in seconds
import time
time.sleep(30)

#BTC Price Data 6
import requests
response = requests.get("https://bitaps.com/api/ticker/average")
pricedata = response.text
lp = pricedata[119:123]
print(lp)

a = int(firstprice)
bp = int(lp)

#BULL vs BEAR Price Spread 3
def market3(a,bp):
    if a < bp:
        return "Bull"
    if a > bp:
        return "Bear"

z = market3(a,bp)

print(z)

mlist = [x,y,z];

print(mlist)

len(mlist)

from collections import Counter
counts = Counter(mlist)
print(counts)

#af is first price taken bp is last price taken
spreaddata = bp - af

print(spreaddata)

sdata = int(spreaddata)

if sdata > 0:
    import os 
os.startfile("C:\\Users\Admin\Documents\GitHub\Bitcoin-ApiData\Bulls.mp4")

if sdata < 0:
    import os 
os.startfile("C:\\Users\Admin\Documents\GitHub\Bitcoin-ApiData\Bears.mp4")


