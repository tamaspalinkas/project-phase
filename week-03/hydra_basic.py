import numpy as np
import pandas as pd
import requests
import json

ids = pd.read_csv('~/greenfox/data-science/week-03/top_movie_ids_1k.csv')
imdb_ids = ids['tconst'].tolist()

url = 'https://hydramovies.com/api-v2/?source=http://hydramovies.com/api-v2/current-Movie-Data.csv&imdb_id='
req_cnt = 0
mv_data = []
names = ['imdb_id', 'Title', 'Categories', 'runtime', 'ytid', 'summary']

for imdb_id in imdb_ids:
    content = requests.get(url + imdb_id).json()
    if not content:
        print(imdb_id + ' failed')
    try:
        for key in content:
            result = {}
            for name in names:
                if name in content[key]:
                    result[name] = content[key][name]
                else:
                    result[name] = None
            mv_data.append([result[name] for name in names])
            print(str(imdb_id) + ' completed')
    except (IndexError, KeyError, TypeError) as error:
        print(str(imdb_id) + ' failed with: ' + str(error))

mv_df = pd.DataFrame(mv_data)
mv_df.to_csv('~/greenfox/project-phase/week-03/hydra_1k_basic.csv', index=False)