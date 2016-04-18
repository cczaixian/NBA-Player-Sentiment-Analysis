import pandas as pd
import json
import glob
df_list=[]
for file in glob.glob('gamelog/*.json'):
    

    json_data=open(file).read()

    data = json.loads(json_data)

    df = pd.DataFrame.from_dict(data['resultSets'][0]['rowSet'])
    df.columns = data['resultSets'][0]['headers']


    df_list.append(df)

frame = pd.concat(df_list)