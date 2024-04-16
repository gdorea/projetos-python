import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = "8ATHPDDLFGHVTR91"
API_KEY_NEWS = "2e5b729e8d954bb5b7327d1f96f1f01a"

response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_KEY_STOCK}")
response.raise_for_status()
data = response.json()
#yesterday = data["Time Series (Daily)"]["2024-04-12"]["4. close"]
#day_before_yesterday = data["Time Series (Daily)"]["2024-04-11"]["4. close"]

response_news = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2024-04-15&sortBy=publishedAt&apiKey={API_KEY_NEWS}")
response_news.raise_for_status()
data_news = response_news.json()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#percentage = ((float(day_before_yesterday) / float(yesterday)) - 1) * 100

#if day_before_yesterday > yesterday:
#    percentage = percentage * -1
#else:
#    percentage = percentage

#if percentage > 2 or percentage < -2:
#    pass


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

for n in range(3):
    print(f"{STOCK}: %")
    print("Headline: ", data_news["articles"][n]["title"])
    print("Brief: ", data_news["articles"][n]["description"])
    n =+ 1

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

