import pandas as pd

df = pd.read_csv('../results.csv', encoding='ISO-8859-1')
df_00_to_20 = df[(df['Season'] >= '2000-01') & (df['Season'] < '2021-22')]

def df_filtered(name):
    df_home_data = df_00_to_20.loc[df_00_to_20['HomeTeam'] == name, ['Season', 'FTR']]['FTR'].value_counts()
    df_home_data.rename(index={'H':'WS', 'A':'DF', 'D':'DW'}, inplace=True)
    
    df_away_data = df_00_to_20.loc[df_00_to_20['AwayTeam'] == name, ['Season', 'FTR']]['FTR'].value_counts()
    
    df_home_data['WS'] += df_away_data['A']
    df_home_data['DF'] += df_away_data['H']
    df_home_data['DW'] += df_away_data['D']

    return df_home_data.sort_index()
