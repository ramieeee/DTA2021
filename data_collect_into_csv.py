import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import datetime

def data_collect(start_num, end_num):
    df = pd.DataFrame(columns=['date','text'])

    for i in range(start_num, end_num + 1):
        url = 'https://www.dentalarirang.com/news/articleView.html?idxno=%s' %str(i)
        try:
            header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
            html = requests.get(url, headers=header, timeout=2).text
            soup = BeautifulSoup(html, "html.parser")

            # 내용 추출
            html_text = str(soup.find_all('p'))

            # 태그 제거
            tags = ['<br/>', '<p>', '</p>', '\r', '\n', '\xa0', '&lt', '<strong>', '</strong>', '&gt']
            for i in range(len(tags)):
                html_text = html_text.replace(tags[i],"").strip()
        
            # 날짜 추출
            date_text = soup.find('ul', 'no-bullet auto-marbtm-0 line-height-6').text
            date_loc = date_text.find('2021')
            date = date_text[date_loc:date_loc + 10]

            # pandas DataFrame에 index 추가하기
            new_data = {'date' : date,
                        'text' : html_text
            }
            df = df.append(new_data, ignore_index=True)
        except:
            pass
    # csv 파일로 저장
    now = str(datetime.datetime.now())
    now_only_date = now[:10].replace('-','')
    df.to_csv(now_only_date + "_data.csv", mode='w')

data_collect(30509, 30513)