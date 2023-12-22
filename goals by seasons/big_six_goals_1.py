import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

df_arsenal_per_season = df_filtered('Arsenal')
df_chelsea_per_season = df_filtered('Chelsea')
df_liverpool_per_season = df_filtered('Liverpool')
df_man_city_per_season = df_filtered('Man City')
df_man_united_per_season = df_filtered('Man United')
df_tottenham_per_season = df_filtered('Tottenham')

fig, ax = plt.subplots(2, 3, figsize=(8, 5))

fig.suptitle('Bix six goals')
fig.supxlabel('Seasons')
fig.supylabel('Goals')
plt.subplots_adjust(hspace=0.4)

ax[0, 0].bar(df_arsenal_per_season['Season'], df_arsenal_per_season['TGS'], label='Total goals scored', color='#002A74ff')
ax[0, 0].bar(df_arsenal_per_season['Season'], df_arsenal_per_season['TGC'], label='Total goals conceded', color='#DB0000ff')
ax[0, 0].set_title('Arsenal')

ax[0, 1].bar(df_chelsea_per_season['Season'], df_chelsea_per_season['TGS'], label='Total goals scored', color='#002A74ff')
ax[0, 1].bar(df_chelsea_per_season['Season'], df_chelsea_per_season['TGC'], label='Total goals conceded', color='#E3B841')
ax[0, 1].set_title('Chelsea')

ax[0, 2].bar(df_liverpool_per_season['Season'], df_liverpool_per_season['TGS'], label='Total goals scored', color='#01977F')
ax[0, 2].bar(df_liverpool_per_season['Season'], df_liverpool_per_season['TGC'], label='Total goals conceded', color='#D10112')
ax[0, 2].set_title('Liverpool')

ax[1, 0].bar(df_man_city_per_season['Season'], df_man_city_per_season['TGS'], label='Total goals scored', color='#033061ff')
ax[1, 0].bar(df_man_city_per_season['Season'], df_man_city_per_season['TGC'], label='Total goals conceded', color='#7BB1DDff')
ax[1, 0].set_title('Man City')

ax[1, 1].bar(df_man_united_per_season['Season'], df_man_united_per_season['TGS'], label='Total goals scored', color='#DA0106ff')
ax[1, 1].bar(df_man_united_per_season['Season'], df_man_united_per_season['TGC'], label='Total goals conceded', color='#FFE600ff')
ax[1, 1].set_title('Man United')

ax[1, 2].bar(df_tottenham_per_season['Season'], df_tottenham_per_season['TGS'], label='Total goals scored', color='#001B57ff')
ax[1, 2].bar(df_tottenham_per_season['Season'], df_tottenham_per_season['TGC'], label='Total goals conceded', color='#dcdddc')
ax[1, 2].set_title('Tottenham')

for i in range(2):
    for j in range(3):
        ax[i, j].set_xticks(df_arsenal_per_season.loc[np.linspace(0, len(df_arsenal_per_season)-1, 3, dtype=int), 'Season'])
        ax[i, j].set_yticks(np.arange(10, 111, 10), minor=True)
        ax[i, j].tick_params(axis='both', labelsize=8)

plt.savefig('plots/big_six_goals_1.png')
plt.show()