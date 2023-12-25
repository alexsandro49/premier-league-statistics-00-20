import pandas as pd
import matplotlib.pyplot as plt
from main import df_filtered

teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Man United', 'Tottenham']
df_big_six_per_team = pd.DataFrame({
    'TEAM': [i for i in teams],
    'HS': [df_filtered(i)['HS'].sum() for i in teams], 
    'HST': [df_filtered(i)['HST'].sum() for i in teams],
    'TGS': [df_filtered(i)['TGS'].sum() for i in teams]
})

df_big_six_per_team.sort_values('HS', inplace=True)

total_shots = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['HS'], label='Total shots', color='#002A74ff')
total_shots_on_target = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['HST'], label='Total shots on target', color='#00967F')
total_goals_scored = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['TGS'], label='Total goals scored', color='#DAA500')
plt.title('Big six shots accuracy')

for i in range(len(total_shots_on_target)):
    plt.text(total_shots[i].get_width() / 2 + total_shots_on_target[i].get_width() / 2, total_shots[i].get_y() + total_shots[i].get_height() / 2, int(df_big_six_per_team.loc[i, 'HS']), ha='center', va='center', fontweight='bold', color='w')
    plt.text(total_goals_scored[i].get_width() + (total_shots_on_target[i].get_width() - total_goals_scored[i].get_width()) / 2, total_shots[i].get_y() + total_shots[i].get_height() / 2, int(df_big_six_per_team.loc[i, 'HST']), ha='center', va='center', fontweight='bold', color='w')
    plt.text(total_goals_scored[i].get_width() / 2, total_shots[i].get_y() + total_shots[i].get_height() / 2, int(df_big_six_per_team.loc[i, 'TGS']), ha='center', va='center', fontweight='bold', color='w')

plt.xticks([])
plt.yticks(fontsize=8)
plt.legend(ncol=3, loc='lower left', bbox_to_anchor=(0, -0.1), fontsize=9)
plt.tight_layout()
plt.savefig('plots/big_six_shots_2.png')
plt.show()