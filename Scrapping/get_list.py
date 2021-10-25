import time
from tqdm import tqdm
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml


url = 'https://careertool.jobagent.ch/module1/a_z.php?StartLetter=&StartRow=880'

arr = []

for page in tqdm(range(0, 881, 10)):
    url = f'https://careertool.jobagent.ch/module1/a_z.php?StartLetter=&StartRow={page}'

    res = requests.get(url)
    print(res.status_code)
    src = res.content
    soup = BeautifulSoup(src, 'lxml')

    mydivs = soup.findAll('a')

    for i in mydivs:
        if 'info.php?' in i.attrs['href']:
            arr.append([i.text, 'https://careertool.jobagent.ch/module1/' + i.attrs['href']])
    time.sleep(1)

df = pd.DataFrame(arr, columns=['name', 'url'])
df.to_csv('list2.csv', index=False, encoding='utf-8')

