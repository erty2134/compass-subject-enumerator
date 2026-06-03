import sys
import requests
from dotenv import load_dotenv, dotenv_values
import os
import re
import time
import random

load_dotenv()

#start: int = 1444
start: int = 1524
#end: int = 1745
end: int = 1927
interval = 0.5
randomness = 0.2
output_file = open("out.txt", 'a')

with requests.Session() as session:
    # enter compass
    compass_cookies = config = dotenv_values(".env")
    url = "https://maristeastwood-nsw.compass.education/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    session.get(url, headers=header, cookies=compass_cookies)
    
    # get all classes, (?<=).*?(?=)
    subject_pattern = r'(?<=<div class="pageHero-title" data-test="hero-title" id="heroTitle">).*?(?=</div>)'
    subject_code_pattern = r'(?<=<div class="pageHero-subtitle">).*?(?=</div>)'
    try:
        for i in range(start, end+1):
            time.sleep(random.uniform(interval-randomness, interval+randomness))

            url = f"https://maristeastwood-nsw.compass.education/Organise/Subjects/Subject.aspx?subjectId={i}"
            response = session.get(url, headers=header, cookies=compass_cookies)

            try:
                subject_match = re.search(subject_pattern, response.text).group()
            except AttributeError:
                subject_match = "not found"
            try:
                subject_code_match = re.search(subject_code_pattern, response.text).group()
            except AttributeError:
                subject_code_match = "not found"

            output = f"id: '{i}', https code: '{response.status_code}', class: '{subject_match}', subject code: '{subject_code_match}'"
            print(output)
            output_file.write(output+"\n")
            output_file.flush()
    except KeyboardInterrupt:
        pass
    finally:
         output_file.close()