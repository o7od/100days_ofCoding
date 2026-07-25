import requests
import requests_cache
import os
from dotenv import load_dotenv
from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages import WhatsappText

requests_cache.install_cache('stock_cache')

load_dotenv()

def calculate_change(new_value: float, old_value: float) -> float:
    """calculates the percent change from the given two inputs"""
    change: float = 100*((new_value - old_value)/old_value)
    change = round(change, 2)
    output: str = ""
    if "-" in str(change):
        decreased_change: str = str(change).split("-")[1]
        output = f"Tesla Stock has seen {change}% decrease🥴 yesterday\n"
    else:
        output = f"Tesla Stock has seen {change}% increase💸 yesterday\n"
    
    return output
    

def get_stock_info(url: str, params: dict) -> tuple:
    """Gets stock info and return a tuple containing its open and close values from yesterday"""
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    data: dict = response.json()["Time Series (Daily)"]
    yesterday_date: str = response.json()["Meta Data"]["3. Last Refreshed"]
    source: str = 'CACHE' if getattr(response, 'from_cache', False) else 'API'
    print("Source: " + source)
    return (data[yesterday_date]["1. open"], data[yesterday_date]["4. close"], yesterday_date)


def get_news_info(news_url: str, params: dict):
    news_article = requests.get(url=news_url, params=params)
    news_article.raise_for_status()
    source: str = 'CACHE' if getattr(news_article, 'from_cache', False) else 'API'
    print("Source: " + source)
    news_source: str = news_article.json()["articles"][0]["source"]["name"]
    description: str = news_article.json()["articles"][0]["description"]
    url: str = news_article.json()["articles"][0]["url"]

    return f"{news_source}: {description}\n{url}"


# 1. Get the daily data about Tesla stock through Alpha advantage API 
STOCK_URL = f"https://www.alphavantage.co/query?"
PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": os.environ.get("STOCK_API"),
}

data: tuple = get_stock_info(STOCK_URL, PARAMS)
change: str = calculate_change(float(data[0]), float(data[1]))

# 2. Get a news about Tesla through news API
NEWS_URL = "https://newsapi.org/v2/everything?"
NEWS_PARAM = {
    "q": "tesla",
    "apiKey": os.environ.get("NEWS_API"),
    "from": data[2], 
    "to": data[2],
    "domains": "bbc.co.uk, techcrunch.com, engadget.com",
}

news: str = get_news_info(NEWS_URL, NEWS_PARAM)

final_text = change + news
# print(final_text)

# 3. send an sms message 

client = Vonage(
    auth=Auth(
        application_id=os.getenv("VONAGE_APPLICATION_ID"),
        private_key=os.getenv("VONAGE_PRIVATE_KEY"),
    ),
    http_client_options=HttpClientOptions(api_host=os.getenv("MESSAGES_SANDBOX_HOST")),
)

message = WhatsappText(
    to=os.getenv("MESSAGES_TO_NUMBER"),
    from_=os.getenv("WHATSAPP_SENDER_ID"),
    text=final_text,
)

response = client.messages.send(message)
print()