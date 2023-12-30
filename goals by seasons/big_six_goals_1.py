import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Man United', 'Tottenham']
df_big_six_goals_by_seasons = [df_filtered(i) for i in teams]

fig, ax = plt.subplots(2, 3, figsize=(8, 5))
fig.suptitle('Bix six goals')
fig.supxlabel('Seasons')
fig.supylabel('Goals')

count = 0
for i in range(2):
    for j in range(3):
        ax[i, j].bar(df_big_six_goals_by_seasons[count]['Season'], df_big_six_goals_by_seasons[count]['TGS'], color='#001B57ff')
        ax[i, j].bar(df_big_six_goals_by_seasons[count]['Season'], df_big_six_goals_by_seasons[count]['TGC'], color='#DB0000ff')
        ax[i, j].set_title(teams[count])
        ax[i, j].set_xticks(df_big_six_goals_by_seasons[count].loc[np.linspace(0, len(df_big_six_goals_by_seasons[count])-1, 3, dtype=int), 'Season'])
        ax[i, j].set_yticks(np.arange(10, 111, 10), minor=True)
        ax[i, j].tick_params(axis='both', labelsize=8)
        count += 1

plt.subplots_adjust(hspace=0.4)
plt.savefig('plots/big_six_goals_1.png')
plt.show()