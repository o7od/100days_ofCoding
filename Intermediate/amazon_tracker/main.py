import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv


load_dotenv()

headers = {
    "User-Agent": os.environ["USER_AGENT"],
    "Accept-Language": os.environ["Accept_Language"],
}


amazon_product_url = "https://www.amazon.com/Sceptre-22-Inch-DisplayPort-Speakers-E225W-FW144/dp/B0FT21HKZ6/ref=sr_1_3?crid=2S7VO2W7NBCT4&dib=eyJ2IjoiMSJ9.GPkg1Ng8j3P6n5EfpkfxZLDsrJ-hbjpSQjlF8aMV-6ov7cXBRmgCQ4oLMVRG-Q76jJdSTrw3_2DBeHzgPW6IA9pGoCoTu9cdFUNFqOUw3M3O_SOtTYmfjo3MXQpC856DwRNXqb6pq4hFGKmTMyQg9capFwslCpQf2c-FYCZIZ0ysgmxplau7LHANO30MeLQUMCgvi24GLGhb9rvPX3VthHqqA8jk_9Nsl-M0cAJ7ljI._VEYR2M6lcCaQTvYjowTka29xojqxQZhdgfRjZvvREI&dib_tag=se&keywords=monitor&qid=1784519565&sprefix=monito%2Caps%2C121&sr=8-3&th=1"


response = requests.get(url=amazon_product_url, headers=headers)
soup = BeautifulSoup(markup=response.text, features="html.parser")

whole_price = soup.find(name="span", class_="a-price-whole")
fraction_price = soup.find(name="span", class_="a-price-fraction")
product_description = soup.find(name="span", id="productTitle")


price_of_product = float(whole_price.getText() + fraction_price.getText())

product_des = product_description.getText()
msg = EmailMessage()
msg["Subject"] =  "Amazon Price Alert"
msg["From"] = "ozodotamirzayev@gmail.com"
msg["To"] = os.environ["MY_EMAIL"]

msg.set_content(f"{product_des} is now: ${price_of_product}")
 
if price_of_product < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.environ["MY_EMAIL"], password=os.environ["MY_PASSWORD"])
        connection.send_message(msg)


