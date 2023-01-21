import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.blocket.se/annonser/stockholm/elektronik/datorer_tv_spel?q=macbook+pro+m1&cg=5020&r=11&st=s"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
time.sleep(5)
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all(
    "h2", class_="TextSubHeading__TextSubHeadingWrapper-sc-1c6hp2-0 kMfrp styled__StyledTitle-sc-1kpvi4z-9 hXHzYV")

for result in results:
    link = results.find(
        "a", class_="Link-sc-6wulv7-0 styled__StyledTitleLink-sc-1kpvi4z-11 cDtkQI buxcTF")
    print(link.text)
    print(link["href"])

print(results)
