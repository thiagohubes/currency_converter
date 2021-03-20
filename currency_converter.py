import requests
import json


from_currency = input()
request_bytes = requests.get(f'http://www.floatrates.com/daily/{from_currency.lower()}.json')
json_dict = json.loads(request_bytes.content)
if from_currency.lower() == 'usd':
    eur_rate = json_dict['eur']['rate']
    rate_dict = dict(eur_rate=eur_rate)
elif from_currency.lower() == 'eur':
    usd_rate = json_dict['usd']['rate']
    rate_dict = dict(usd_rate=usd_rate)
else:
    eur_rate = json_dict['eur']['rate']
    usd_rate = json_dict['usd']['rate']
    rate_dict = dict(usd_rate=usd_rate, eur_rate=eur_rate)
while True:
    to_currency = input()
    if to_currency == '':
        break
    value = float(input())
    print('Checking the cache...')
    if to_currency.lower() + '_rate' in rate_dict.keys():
        print('Oh! It is in the cache!')
        rate = json_dict[to_currency.lower()]['rate']
        converted_currency = value * rate
        print(f'You received {round(converted_currency, 2)} {to_currency}')
    else:
        print('Sorry, but it is not in the cache!')
        rate_dict[to_currency.lower() + '_rate'] = json_dict[to_currency.lower()]['rate']
        rate = rate_dict[to_currency.lower() + '_rate']
        converted_currency = value * rate
        print(f'You received {round(converted_currency, 2)} {to_currency}')
