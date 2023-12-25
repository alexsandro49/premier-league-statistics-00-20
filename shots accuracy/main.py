import pandas as pd

df = pd.read_csv('../results.csv', encoding='ISO-8859-1')
df_00_to_20 = df[(df['Season'] >= '2000-01') & (df['Season'] < '2021-22')]

def df_filtered(name):
    df_filtered = df_00_to_20.loc[df_00_to_20['HomeTeam'] == name, ['Season', 'HS', 'HST', 'FTHG']].groupby('Season').sum().reset_index()
    df_filtered.rename(columns={'FTHG':'TGS'}, inplace=True)
    df_filtered['TGS'] += df_00_to_20[df_00_to_20['AwayTeam'] == name].groupby('Season').sum().reset_index()['FTAG']
    return df_filtered

df_filtered('Arsenal').columns