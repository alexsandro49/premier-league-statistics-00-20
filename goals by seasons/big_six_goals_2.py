import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

df_arsenal_per_season = df_filtered('Arsenal')
df_chelsea_per_season = df_filtered('Chelsea')
df_liverpool_per_season = df_filtered('Liverpool')
df_man_city_per_season = df_filtered('Man City')
df_man_united_per_season = df_filtered('Man United')
df_tottenham_per_season = df_filtered('Tottenham')

df_big_six_per_team = pd.DataFrame({
    'TEAM': ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Man United', 'Tottenham'],
    'TGS': [df_arsenal_per_season['TGS'].sum(), df_chelsea_per_season['TGS'].sum(), df_liverpool_per_season['TGS'].sum(), df_man_city_per_season['TGS'].sum(), df_man_united_per_season['TGS'].sum(), df_tottenham_per_season['TGS'].sum()], 
    'TGC': [df_arsenal_per_season['TGC'].sum(), df_chelsea_per_season['TGC'].sum(), df_liverpool_per_season['TGC'].sum(), df_man_city_per_season['TGC'].sum(), df_man_united_per_season['TGC'].sum(), df_tottenham_per_season['TGC'].sum()],
    'CTGS': ['#002A74ff', '#002A74ff', '#01977F', '#033061ff', '#DA0106ff', '#001B57ff'],
    'CTGC': ['#DB0000ff', '#E3B841', '#D10112', '#7BB1DDff', '#FFE600ff', '#dcdddc']
})

df_big_six_per_team.sort_values('TGS', inplace=True)

total_goals_scored = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['TGS'], color=df_big_six_per_team['CTGS'])
total_goals_conceded = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['TGC'], color=df_big_six_per_team['CTGC'])
plt.title('Big six goals per team')
plt.bar_label(total_goals_scored, label_type='edge', padding=4)
plt.bar_label(total_goals_conceded, label_type='center')
plt.xlabel('Goals')
plt.ylabel('Teams')
plt.xticks(np.arange(100, 1801, 200), minor=True)
plt.rcParams['xtick.labelsize'] = 12
plt.tight_layout()
plt.savefig('plots/big_six_goals_2.png')
plt.show()