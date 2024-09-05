import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

try:

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = r.json()
    bpi = o["bpi"]
    USD = bpi["USD"]
    rate = USD["rate_float"]
    amount = float(sys.argv[1]) * rate


except requests.RequestException:
    pass
print(f"${amount:,.4f}")
