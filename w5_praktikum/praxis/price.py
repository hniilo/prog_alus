import requests
from datetime import datetime

api = 'https://dashboard.elering.ee/api/nps/price?start=2026-09-28T21%3A00%3A00.000Z&end=2026-09-29T20%3A59%3A59.999Z'
response = requests.get(api)
response.raise_for_status()

data = response.json()['data']['ee']   # [{'timestamp': ..., 'price': ...}, ...]

with open("prices.txt", 'w') as f:
    for el in data:
        t = datetime.fromtimestamp(el['timestamp'])   # Unix seconds -> local time
        f.write(f"{t:%Y-%m-%d %H:%M}\t{el['price']}\n")