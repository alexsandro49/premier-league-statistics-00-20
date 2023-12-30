import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Man United', 'Tottenham']
df_big_six_shots_accuracy = [df_filtered(i) for i in teams]
df_big_six_shots_accuracy = [i.loc[np.linspace(0, len(i)-1, 5, dtype=int), :] for i in df_big_six_shots_accuracy]

fig, ax = plt.subplots(2, 3, figsize=(8, 5))
fig.suptitle('Bix six shots accuracy')
fig.supxlabel('Seasons')
fig.supylabel('Shots')

indexes = np.arange(5)
bar_width = 0.25

count = 0
for i in range(2):
    for j in range(3):
        ax[i, j].bar(indexes, df_big_six_shots_accuracy[count]['TS'], width=bar_width, color='#002A74ff')
        ax[i, j].bar([i + bar_width for i in indexes], df_big_six_shots_accuracy[count]['TST'], width=bar_width, color='#DB0000ff')
        ax[i, j].bar([i + 2*bar_width for i in indexes], df_big_six_shots_accuracy[count]['TGS'], width=bar_width, color='#9C824A')
        ax[i, j].set_title(teams[count])        
        ax[i, j].set_xticks([k + bar_width for k in np.arange(0, 5, 2)], df_filtered('Arsenal').loc[np.arange(0, 6, 2, dtype=int), 'Season'])
        ax[i, j].set_yticks(np.arange(100, 751, 200), minor=True)
        ax[i, j].set_ylim(0, 850)
        ax[i, j].tick_params(axis='both', labelsize=8)
        count += 1

plt.subplots_adjust(hspace=0.4)
plt.savefig('plots/big_six_shots_1.png')
plt.show()