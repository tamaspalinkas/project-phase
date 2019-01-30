import numpy as np
import pandas as pd
import requests
import json
from multiprocessing import Pool, Manager
import re

ids = pd.read_csv('~/greenfox/data-science/week-03/top_movie_ids_1k.csv')
imdb_ids = ids['tconst'].tolist()

url = 'https://hydramovies.com/api-v2/?source=http://hydramovies.com/api-v2/current-Movie-Data.csv&imdb_id='
req_cnt = 0
mv_data = []

testlist = imdb_ids[:6]

def get_mv_data(mv_list, L):
    imdb_ids = mv_list
    for imdb_id in imdb_ids:
        content = requests.get(url + imdb_id).json()
        if not content:
            print(imdb_id + ' failed')
        try:
            for key in content:
                for item in content.items():
                    L.append([content[key]['imdb_id'], content[key]['Title'],
                    content[key]['Categories'], content[key]['runtime'], content[key]['ytid'], content[key]['summary']])
                    print(str(imdb_id) + ' completed')
        except (IndexError, KeyError, TypeError) as error:
            print(str(imdb_id) + ' failed with: ' + str(error))
    return L

if __name__ == '__main__':
    with Manager() as manager:
        L = manager.list()
        pool = Pool(processes=2)
        r1 = pool.apply_async(get_mv_data, [testlist[:3], L])
        r2 = pool.apply_async(get_mv_data, [testlist[3:], L])
        pool.close()
        pool.join()
        df = pd.DataFrame(list(L))
        print(df.head())