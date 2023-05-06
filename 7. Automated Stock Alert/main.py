import requests
from twilio.rest import Client

# Put it on pythoneanywhere if want to
# Mostly stock names are 4 digit
# google = GOOG   # Microsoft = MSFT   # apple = AAPL

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# AN API to get the stock prices
ALPHA_VANTAGE_API_KEY = "T2S6D7FWY6CQ4HH1"
STOCK_ENDPOINT_ULR = "https://www.alphavantage.co/query"

stock_parameter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}


responses = requests.get(STOCK_ENDPOINT_ULR, params=stock_parameter)
responses.raise_for_status()
data = responses.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]  # Try to understand  # Really important
yesterday_stock_price = data_list[0]["4. close"]
day_before_yesterday_stock_price = data_list[1]["4. close"]

print(f"day before yesterday stock = {day_before_yesterday_stock_price}")
print(f"day before yesterday stock = {yesterday_stock_price}")

# Positive difference
difference = float(yesterday_stock_price) - float(day_before_yesterday_stock_price)
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔻"

# Difference percentage
diff_percentage = round(difference/float(yesterday_stock_price) * 100)
print(diff_percentage)


## STEP 2: Use https://newsapi.org
NEWS_API_KEY = "1652c51826784331949ac869d3cc12dd"
NEWS_API_URL = "https://newsapi.org/v2/everything?"  #q=tesla&from=2022-12-10&sortBy=publishedAt&apiKey=1652c51826784331949ac869d3cc12dd

news_parameter = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}
if abs(diff_percentage) > 5:
    respond = requests.get(NEWS_API_URL, params=news_parameter)
    respond.raise_for_status()
    news = respond.json()["articles"]
    three_articles = news[:3]

    formatted_article = [f"{STOCK}: {up_down}{diff_percentage}%\nHeading: {article['title']}.\n\nBrief: {article['description']}" for article in three_articles]
    print(formatted_article)


    # whatsapp
    Account_SID = "ACc3b4dd6888464ce6dcf3ef0edb2c4d64"  # like username
    Auth_Token = "2e02b3cc185c550dec890a8fd05d7db6"  # like password

    client = Client(Account_SID, Auth_Token)

    from_whatsapp_number = "whatsapp:+14155238886"
    to_whatsapp_number = "whatsapp:+9477YOUR PHONE NUMBER"

    for article in formatted_article:
        client.messages.create(
            body=article,
            from_=from_whatsapp_number,
            to=to_whatsapp_number)




