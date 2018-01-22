import pandas as pd

def load(file_name = "../data/external/condensed_2016.json.zip"):

    all_data = pd.read_json(file_name)

    return all_data

def label(data):
    data = data.loc[data['source'] != 'Twitter Ads']

    # insert new column
    data['isTrump'] = [True if x == 'Twitter for Android' else False for x in data['source']]
    
    return data