import pandas as pd

df = pd.read_csv('../results.csv', encoding='ISO-8859-1')
df_00_to_20 = df[(df['Season'] >= '2000-01') & (df['Season'] < '2021-22')]

def df_filtered(name):
    df_home_data = df_00_to_20.loc[df_00_to_20['HomeTeam'] == name, ['Season', 'HS', 'HST', 'FTHG']].groupby('Season').sum().reset_index()
    df_home_data.rename(columns={'HS':'TS', 'HST':'TST', 'FTHG':'TGS'}, inplace=True)

    df_away_data = df_00_to_20.loc[df_00_to_20['AwayTeam'] == name, ['Season', 'AS', 'AST', 'FTAG']].groupby('Season').sum().reset_index()
    
    df_home_data['TS'] += df_away_data['AS']
    df_home_data['TST'] += df_away_data['AST']
    df_home_data['TGS'] += df_away_data['FTAG']
    
    return df_home_data