import time
from tqdm import tqdm
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml
import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = cleantext.replace('[', '')
    cleantext = cleantext.replace(']', '')
    return cleantext


df = pd.read_csv('../Data/Scraped_data/list.csv')
arr = []
c = 0

for i, r in df.iterrows():
    print(r['name'], r['url'])

    name = r['name']
    url = r['url']
    url = 'https://careertool.jobagent.ch/module1/info.php?BerufsID=35456'

    res = requests.get(url)
    print(res.status_code)
    src = res.content
    soup = BeautifulSoup(src, 'lxml')

    unknown = ''
    Berufs = ''
    Rubriken = ''
    Synonyme = ''
    Verwandte = ''

    try:
        unknown = soup.find('span', {'class': 'content_text_italic'}).text
        unknown = unknown.replace('\n', '')
        unknown = unknown.replace('\t', '')
        # print(unknown)
    except Exception as e:
        print(e)
        unknown = ''

    try:
        Berufs = soup.select('.content table td:nth-child(1) tr:nth-child(2) td')
        Berufs = cleanhtml(str(Berufs))
        Berufs = ' '.join(Berufs.split())
        # print(Berufs)
    except Exception as e:
        print(e)
        Berufs = ''

    try:
        Rubriken = str(soup.select('tr:nth-child(4) ul'))

        t = Rubriken.split('<li>')
        a = []
        for x in t:
            y = cleanhtml(x)
            if len(y) > 0:
                a.append(y)
        Rubriken = a
        # print(Rubriken)
    except Exception as e:
        print(e)
        Rubriken = []

    try:
        Synonyme = cleanhtml(str(soup.select('tr~ tr+ tr p')))
        print("==> ", Synonyme)
    except Exception as e:
        print(e)
        Synonyme = ''

    try:
        Verwandte = str(soup.select('.content table td:nth-child(1) tr:nth-child(6) td'))
        t = Verwandte.split('<li>')
        a = []
        for x in t:
            y = cleanhtml(x)
            if len(y) > 0:
                a.append(y)
        Verwandte = a
        # print(Verwandte)
    except Exception as e:
        print(e)
        Verwandte = []

    arr.append([name, unknown, Berufs, Synonyme, Rubriken, Verwandte])
    print([name, unknown, Berufs, Synonyme, Rubriken, Verwandte])

    c += 1
    if c > 0:
        break

