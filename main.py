import requests
from dotenv import load_dotenv, dotenv_values
import os
import re
import time
import random

load_dotenv()

start: int = 1650
#end: int = 1745
end: int = 1745
interval = 0.5
randomness = 0.2

with requests.Session() as session:
    # enter compass
    compass_cookies = config = dotenv_values(".env")
    url = "https://maristeastwood-nsw.compass.education/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    session.get(url, headers=header, cookies=compass_cookies)
    
    # get all classes
    pattern = r'(?<=<div class="pageHero-title" data-test="hero-title" id="heroTitle">).*?(?=</div>)'
    for i in range(start, end+1):
        time.sleep(random.uniform(interval-randomness, interval+randomness))
        url = f"https://maristeastwood-nsw.compass.education/Organise/Subjects/Subject.aspx?subjectId={i}"
        response = session.get(url, headers=header, cookies=compass_cookies)
        match = re.search(pattern, response.text)
        #print(f"code: {response.status_code}, id: {i}")
        print(f"code: {response.status_code}, class: {match.group()}, id: {i}")