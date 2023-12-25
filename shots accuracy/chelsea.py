import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

df_chelsea_shots_accuracy = df_filtered('Chelsea')
df_chelsea_shots_accuracy = df_chelsea_shots_accuracy.loc[np.linspace(0, len(df_chelsea_shots_accuracy)-1, 5, dtype=int), :]
indexes = np.arange(5)
bar_width = 0.25

total_shots = plt.bar(indexes, df_chelsea_shots_accuracy['HS'], width=bar_width, label='Total shots', color='#153D8A')
total_shots_on_target = plt.bar([i + bar_width for i in indexes], df_chelsea_shots_accuracy['HST'], width=bar_width, label='Total shots on target', color='#728AB9')
total_goals_scored = plt.bar([i + 2*bar_width for i in indexes], df_chelsea_shots_accuracy['TGS'], width=bar_width, label='Total goals scored', color='#E30613')
plt.title('Chelsea shots accuracy')
plt.xlabel('Seasons')
plt.ylabel('Shots')
plt.bar_label(total_shots, color='#153D8A', padding=1, fontsize=7, fontweight='bold')
plt.bar_label(total_shots_on_target, color='#153D8A', padding=1, fontsize=7, fontweight='bold')
plt.bar_label(total_goals_scored, color='#153D8A', padding=1, fontsize=7, fontweight='bold')
plt.xticks([i + bar_width for i in indexes], df_chelsea_shots_accuracy['Season'])
plt.yticks(np.arange(25, 426, 50), minor=True)
plt.ylim(0, 450)
plt.legend(loc='upper left', ncols=3, fontsize=9)
plt.savefig('plots/chelsea_shots_accuracy.png')
plt.show()