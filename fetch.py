from feeder import fetch
import requests
from bs4 import BeautifulSoup


ENDPOINT = "https://coinmarketcap.com/"

def fetch_single():
    net_worth = 0
    count=0
    for i in fetch:
        count=count+1
        flag=1
        while flag==1:
            not_found_data = requests.get(ENDPOINT +"currencies/"+ i["currency"]+"/")
            soup = BeautifulSoup(not_found_data.text, features="lxml")
            single_price = soup.find("span", {"id":"quote_price"})
            if single_price:
               flag=2 
        cyrpto_worth = i["holding"] * float(single_price["data-usd"])
        net_worth = net_worth + cyrpto_worth
        print count," ",i["currency"]," : ", str(cyrpto_worth)
    return net_worth   
net_worth = fetch_single()
print "\n\n"

print "Net Worth"," : ", net_worth