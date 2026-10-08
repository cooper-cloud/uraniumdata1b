"""Writes site/data/prices.json from Yahoo (yfinance). Keeps last good value if a ticker fails."""
import json, datetime, yfinance as yf
P="site/data/prices.json"
try: old=json.load(open(P))["prices"]
except Exception: old={}
new={}
for t in json.load(open("site/data/5b.json"))["companies"]:
    sym=t.split(":")[1]+".AX"
    try:
        fi=yf.Ticker(sym).fast_info
        new[t]={"price":fi["last_price"],"mcap":fi["market_cap"],"hi52":fi["year_high"],"lo52":fi["year_low"],"stale":False}
    except Exception as e:
        print("failed",sym,e)
        if t in old: new[t]={**old[t],"stale":True}
json.dump({"as_of":datetime.datetime.utcnow().isoformat()+"Z","prices":new},open(P,"w"))
