import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

df_tottenham_shots_accuracy = df_filtered('Tottenham')
df_tottenham_shots_accuracy = df_tottenham_shots_accuracy.loc[np.linspace(0, len(df_tottenham_shots_accuracy)-1, 5, dtype=int), :]
indexes = np.arange(5)
bar_width = 0.25

total_shots = plt.bar(indexes, df_tottenham_shots_accuracy['HS'], width=bar_width, label='Total shots', color='#001B57ff')
total_shots_on_target = plt.bar([i + bar_width for i in indexes], df_tottenham_shots_accuracy['HST'], width=bar_width, label='Total shots on target', color='#dcdddc')
total_goals_scored = plt.bar([i + 2*bar_width for i in indexes], df_tottenham_shots_accuracy['TGS'], width=bar_width, label='Total goals scored', color='#8a7470')
plt.title('Tottenham shots accuracy')
plt.xlabel('Seasons')
plt.ylabel('Shots')
plt.bar_label(total_shots, color='#001B57ff', padding=1, fontsize=7, fontweight='bold')
plt.bar_label(total_shots_on_target, color='#001B57ff', padding=1, fontsize=7, fontweight='bold')
plt.bar_label(total_goals_scored, color='#001B57ff', padding=1, fontsize=7, fontweight='bold')
plt.xticks([i + bar_width for i in indexes], df_tottenham_shots_accuracy['Season'])
plt.yticks(np.arange(25, 426, 50), minor=True)
plt.ylim(0, 450)
plt.legend(loc='upper left', ncols=3, fontsize=9)
plt.savefig('plots/tottenham_shots_accuracy.png')
plt.show()