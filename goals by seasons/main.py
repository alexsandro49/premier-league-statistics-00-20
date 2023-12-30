import pandas as pd

df = pd.read_csv('../results.csv', encoding='ISO-8859-1')
df_00_to_21 = df[(df['Season'] >= '2000-01') & (df['Season'] < '2021-22')]

def df_filtered(name):
    df_home_data = df_00_to_21.loc[df_00_to_21['HomeTeam'] == name, ['Season', 'FTHG', 'FTAG']].groupby('Season').sum().reset_index()
    df_home_data.rename(columns={'FTHG':'TGS', 'FTAG':'TGC'}, inplace=True)
    
    df_away_data = df_00_to_21[df_00_to_21['AwayTeam'] == name].groupby('Season').sum().reset_index()

    df_home_data['TGS'] += df_away_data['FTAG']
    df_home_data['TGC'] += df_away_data['FTHG']
    
    return df_home_data