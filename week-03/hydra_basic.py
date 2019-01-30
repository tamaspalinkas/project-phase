import numpy as np
import pandas as pd
import requests
import json

ids = pd.read_csv('~/greenfox/data-science/week-03/top_movie_ids_1k.csv')
imdb_ids = ids['tconst'].tolist()

url = 'https://hydramovies.com/api-v2/?source=http://hydramovies.com/api-v2/current-Movie-Data.csv&imdb_id='
req_cnt = 0
mv_data = []
testlist = imdb_ids[:5]

for imdb_id in testlist:
    content = requests.get(url + imdb_id).json()
    if not content:
        print(imdb_id + ' failed')
    try:
        for key in content:
            for item in content.items():    
                mv_data.append([content[key]['imdb_id'], content[key]['Title'],
                content[key]['Categories'], content[key]['runtime'], content[key]['ytid'], content[key]['summary']])
                print(str(imdb_id) + ' completed')
    except (IndexError, KeyError, TypeError) as error:
        print(str(imdb_id) + ' failed with: ' + str(error))

print(mv_data)
mv_df = pd.DataFrame(mv_data)
print(mv_df.head())
mv_df.to_csv('~/greenfox/project-phase/week-03/mp_test.csv', index=False)