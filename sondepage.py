import requests
from bs4 import BeautifulSoup

url = "https://www.moniteurlive.com/auctions/future"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

with open("resultats.txt", "w") as f:
    for tag in soup.find_all(True):
        if tag.has_attr("id"):
            f.write(f"ID: {tag['id']}\n")
        if tag.has_attr("class"):
            f.write(f"Classes: {', '.join(tag['class'])}\n")
