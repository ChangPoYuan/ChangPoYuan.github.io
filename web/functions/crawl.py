# 一週的天氣預測

import requests
from bs4 import BeautifulSoup
import re

def rain_predict():
    url = "https://www.cwa.gov.tw/V8/C/W/County/MOD/Week/63_Week_m.html?T=2024031313-1"
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    imgs = soup.find_all('img')
    alt_texts = [img['alt'] for img in imgs]
    alt_morning = []  # 用來收集白天的天氣
    for i in range(len(alt_texts)):
        if i % 2 == 0:
            alt_morning.append(alt_texts[i])
    # print(alt_morning[0])

    # 正規表達判斷有無雨字代表是否會有降雨
    pattern = re.compile(r'雨')
    match = pattern.search(alt_morning[0])
    rain_T_F = ''
    if match:
        rain_T_F = 'T'
    else:
        rain_T_F = 'F'
    return rain_T_F
