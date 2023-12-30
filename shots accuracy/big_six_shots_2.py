import pandas as pd
import matplotlib.pyplot as plt
from main import df_filtered

teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Man United', 'Tottenham']
df_big_six_per_team = pd.DataFrame({
    'TEAM': [i for i in teams],
    'TS': [df_filtered(i)['TS'].sum() for i in teams], 
    'TST': [df_filtered(i)['TST'].sum() for i in teams],
    'TGS': [df_filtered(i)['TGS'].sum() for i in teams]
})
df_big_six_per_team.sort_values('TS', inplace=True)

total_shots = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['TS'], label='Total shots', color='#002A74ff')
total_shots_on_target = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['TST'], label='Total shots on target', color='#00967F')
total_goals_scored = plt.barh(df_big_six_per_team['TEAM'], df_big_six_per_team['TGS'], label='Total goals scored', color='#DAA500')
plt.title('Big six shots accuracy')

for i in range(len(total_shots_on_target)):
    plt.text(total_shots[i].get_width() / 2 + total_shots_on_target[i].get_width() / 2, total_shots[i].get_y() + total_shots[i].get_height() / 2, int(df_big_six_per_team.loc[i, 'TS']), ha='center', va='center', fontweight='bold', color='w')
    plt.text(total_goals_scored[i].get_width() + (total_shots_on_target[i].get_width() - total_goals_scored[i].get_width()) / 2, total_shots[i].get_y() + total_shots[i].get_height() / 2, int(df_big_six_per_team.loc[i, 'TST']), ha='center', va='center', fontweight='bold', color='w')
    plt.text(total_goals_scored[i].get_width() / 2, total_shots[i].get_y() + total_shots[i].get_height() / 2, int(df_big_six_per_team.loc[i, 'TGS']), ha='center', va='center', fontweight='bold', color='w')

plt.xticks([])
plt.yticks(fontsize=8)
plt.legend(ncol=3, loc='lower left', bbox_to_anchor=(0, -0.1), fontsize=9)
plt.tight_layout()
plt.savefig('plots/big_six_shots_2.png')
plt.show()