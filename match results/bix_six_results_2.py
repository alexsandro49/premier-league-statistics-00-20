import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Man United', 'Tottenham']
df_big_six_per_team = pd.DataFrame({
    'TEAM': [i for i in teams],
    'WS': [df_filtered(i)['WS'] for i in teams], 
    'DW': [df_filtered(i)['DW'] for i in teams],
    'DF': [df_filtered(i)['DF'] for i in teams]
})

df_big_six_per_team.sort_values('WS', ascending=False, inplace=True)
indexes = np.arange(6)
bar_width = 0.25

total_victories = plt.bar(indexes, df_big_six_per_team['WS'], width=bar_width, label='Total victories', color='#002A74ff')
total_draws = plt.bar([i + bar_width for i in indexes], df_big_six_per_team['DW'], width=bar_width, label='Total draws', color='#00967F')
total_defeats = plt.bar([i + 2*bar_width for i in indexes], df_big_six_per_team['DF'], width=bar_width, label='Total defeats', color='#DB0000ff')

plt.title('Big six match results')
plt.bar_label(total_victories, color='#001B57ff', padding=1, fontsize=7, fontweight='bold')
plt.bar_label(total_draws, color='#001B57ff', padding=1, fontsize=7, fontweight='bold')
plt.bar_label(total_defeats, color='#001B57ff', padding=1, fontsize=7, fontweight='bold')
plt.ylim(0, 600)
plt.xticks([i + bar_width for i in indexes], df_big_six_per_team['TEAM'])
plt.yticks(np.arange(50, 651, 100), minor=True, fontsize=8)
plt.legend(loc='upper center', ncols=3, fontsize=9)
plt.tight_layout()
plt.savefig('plots/big_six_results_2.png')
plt.show()