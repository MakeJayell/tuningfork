from bs4 import BeautifulSoup

import requests
import time


url = "http://pitchfork.com/reviews/best/albums"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
results = ""
title = soup.p
h1 = soup.h1
h2 = soup.h2


maindiv = soup.find_all("div", {"id": "main"})


for h3 in maindiv:
    print(h3)

