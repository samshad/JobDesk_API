import time
from tqdm import tqdm
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml
from lxml import html
import re
import os


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = cleantext.replace('[', '')
    cleantext = cleantext.replace(']', '')
    return cleantext


df = pd.read_csv('../Data_files/Scraped_data/list.csv')
arr = []
c = 0

files = os.listdir('../Data_files/Scraped_data/Individual_Files/')

for i, r in df.iterrows():
    print(r['name'], r['url'])

    name = r['name']
    name = name.replace('/', '_')
    url = r['url']
    # url = 'https://careertool.jobagent.ch/module1/info.php?BerufsID=35456'
    if name + '.csv' not in files:
        res = requests.get(url)
        print(res.status_code)
        # src = res.content
        src = res.text
        soup = BeautifulSoup(src, 'html.parser')

        table = soup.findAll('table')[9]

        data = dict()
        flag = 0

        unknown = ''
        try:
            unknown = soup.find('span', class_='content_text_italic').text.strip()
        except:
            unknown = ''

        data['profession'] = name
        data['unknown'] = unknown

        # print(table)
        rows = table.findAll('tr')
        x = ''

        for row in rows:
            if flag == 0:
                flag = 1
                x = row.find('td').text.strip()
                continue
            else:
                flag = 0
                col = row.find('td')
                uls = col.findAll('ul')
                z = []
                if len(uls) > 0:
                    for ul in uls:
                        lis = ul.findAll('li')
                        for li in lis:
                            # print(li.text)
                            z.append(li.text.strip())
                else:
                    # print(col.text)
                    z = col.text.strip()
                data[x] = z
                x = ''

        tf = pd.json_normalize(data)
        tf.to_csv('../Data_files/Scraped_data/Individual_Files/' + name + '_utf-8.csv', index=False,
                  encoding='utf-8')

        # print(data)
        # arr.append(data)

        # c += 1
        # if c == 5:
        #     break

