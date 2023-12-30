import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

df_man_city_shots_accuracy = df_filtered('Man City')
df_man_city_shots_accuracy = df_man_city_shots_accuracy.loc[np.linspace(0, len(df_man_city_shots_accuracy)-1, 5, dtype=int), :]
indexes = np.arange(5)
bar_width = 0.25

total_shots = plt.bar(indexes, df_man_city_shots_accuracy['TS'], width=bar_width, label='Total shots', color='#002A5A')
total_shots_on_target = plt.bar([i + bar_width for i in indexes], df_man_city_shots_accuracy['TST'], width=bar_width, label='Total shots on target', color='#7AB2E1')
total_goals_scored = plt.bar([i + 2*bar_width for i in indexes], df_man_city_shots_accuracy['TGS'], width=bar_width, label='Total goals scored', color='#DAA500')
plt.title('Man City shots accuracy')
plt.xlabel('Seasons')
plt.ylabel('Shots')
plt.bar_label(total_shots, color='#002A5A', padding=1, fontsize=7, fontweight='bold')
plt.bar_label(total_shots_on_target, color='#002A5A', padding=1, fontsize=7, fontweight='bold')
plt.bar_label(total_goals_scored, color='#002A5A', padding=1, fontsize=7, fontweight='bold')
plt.xticks([i + bar_width for i in indexes], df_man_city_shots_accuracy['Season'])
plt.yticks(np.arange(50, 751, 100), minor=True)
plt.ylim(0, 850)
plt.legend(loc='upper left', ncols=3, fontsize=9)
plt.savefig('plots/man_city_shots_accuracy.png')
plt.show()