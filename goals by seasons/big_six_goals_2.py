import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Man United', 'Tottenham']
df_big_six_per_team = pd.DataFrame({
    'TEAM': [i for i in teams],
    'TGS': [df_filtered(i)['TGS'].sum() for i in teams],
    'TGC': [df_filtered(i)['TGC'].sum() for i in teams]
})

df_big_six_per_team.sort_values('TGS', inplace=True)

total_goals_scored = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['TGS'], label='Total goals scored', color='#002A74ff')
total_goals_conceded = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['TGC'], label='Total goals conceded', color='#DB0000ff')
plt.title('Big six goals')

for i in range(len(total_goals_scored)):
    plt.text(total_goals_conceded[i].get_width() + (total_goals_scored[i].get_width() - total_goals_conceded[i].get_width()) / 2, total_goals_scored[i].get_y() + total_goals_scored[i].get_height() / 2, int(df_big_six_per_team.loc[i, 'TGS']), ha='center', va='center', fontweight='bold', color='w')
    plt.text(total_goals_conceded[i].get_width() / 2, total_goals_conceded[i].get_y() + total_goals_conceded[i].get_height() / 2, int(df_big_six_per_team.loc[i, 'TGC']), ha='center', va='center', fontweight='bold', color='w')

plt.xticks([])
plt.yticks(fontsize=8)
plt.legend(ncol=2, loc='lower left', bbox_to_anchor=(0, -0.1), fontsize=9)
plt.tight_layout()
plt.savefig('plots/big_six_goals_2.png')
plt.show()