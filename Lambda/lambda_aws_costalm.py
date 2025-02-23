import datetime
import os
import json
import boto3
from dateutil import relativedelta
import urllib.request
import urllib.parse as parse

API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]
GROUP_ID = os.environ["GROUP_ID"]
TELEGRAM_URL = "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)

def get_exchange_rate(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/KRW"
    with urllib.request.urlopen(url) as response:
        source = response.read().decode("utf-8")
        data = json.loads(source)
        exchange_rate = data["conversion_rate"]
        return exchange_rate

def month_to_date_cost(start, end):
    client = boto3.client("ce")
    response = client.get_cost_and_usage(
        TimePeriod={"Start": start, "End": end},
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )
    amount = response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]
    output = "%.2f" % float(amount)
    return str(output)

def lambda_handler(event, context):
    exchange = get_exchange_rate(API_KEY)

    this_month = datetime.datetime.today()
    next_month = this_month + relativedelta.relativedelta(months=1)
    this_month_start = this_month.strftime("%Y-%m-01")
    next_month_start = next_month.strftime("%Y-%m-01")
    total_cost = month_to_date_cost(this_month_start, next_month_start)
    
    total_cost_dollar = float(total_cost)
    total_cost_dollar_formatted = "{:,.2f}".format(total_cost_dollar)
    
    total_cost_main = int(float(total_cost) * exchange)
    total_cost_main_formatted = format(total_cost_main, ',')

    ### Telegram message ###
    message = "[ AWS Cost(Daily) ]\n" \
              + this_month.strftime("● Date : %B-%d-%Y\n") \
              + "● Account : Username\n" \
              + "● Exchange Rate : ₩" + str(exchange) + "\n" \
              + "● Cost(₩) : ₩" + str(total_cost_main_formatted) + " (Month)\n" \
              + "● Cost($) : $" + str(total_cost_dollar_formatted) + " (Month)"

    try:
        data = parse.urlencode({
            "chat_id": GROUP_ID,
            "text": message,
            "parse_mode": "Markdown"
        }).encode()
        req = urllib.request.Request(TELEGRAM_URL, data=data)
        with urllib.request.urlopen(req) as response:
            response.read()
    except Exception as e:
        print(e)