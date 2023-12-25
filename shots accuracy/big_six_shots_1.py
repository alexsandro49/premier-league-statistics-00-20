import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

df_arsenal_shots_accuracy = df_filtered('Arsenal')
df_chelsea_shots_accuracy = df_filtered('Chelsea')
df_liverpool_shots_accuracy = df_filtered('Liverpool')
df_man_city_shots_accuracy = df_filtered('Man City')
df_man_united_shots_accuracy = df_filtered('Man United')
df_tottenham_shots_accuracy = df_filtered('Tottenham')

df_arsenal_shots_accuracy = df_arsenal_shots_accuracy.loc[np.linspace(0, len(df_arsenal_shots_accuracy)-1, 5, dtype=int), :]
df_chelsea_shots_accuracy = df_chelsea_shots_accuracy.loc[np.linspace(0, len(df_chelsea_shots_accuracy)-1, 5, dtype=int), :]
df_liverpool_shots_accuracy = df_liverpool_shots_accuracy.loc[np.linspace(0, len(df_liverpool_shots_accuracy)-1, 5, dtype=int), :]
df_man_city_shots_accuracy = df_man_city_shots_accuracy.loc[np.linspace(0, len(df_man_city_shots_accuracy)-1, 5, dtype=int), :]
df_man_united_shots_accuracy = df_man_united_shots_accuracy.loc[np.linspace(0, len(df_man_united_shots_accuracy)-1, 5, dtype=int), :]
df_tottenham_shots_accuracy = df_tottenham_shots_accuracy.loc[np.linspace(0, len(df_tottenham_shots_accuracy)-1, 5, dtype=int), :]

fig, ax = plt.subplots(2, 3, figsize=(8, 5))

fig.suptitle('Bix six shots accuracy')
fig.supxlabel('Seasons')
fig.supylabel('Shots')
plt.subplots_adjust(hspace=0.4)

indexes = np.arange(5)
bar_width = 0.25

ax[0, 0].bar(indexes, df_arsenal_shots_accuracy['HS'], width=bar_width, label='Total shots', color='#002A74ff')
ax[0, 0].bar([i + bar_width for i in indexes], df_arsenal_shots_accuracy['HST'], width=bar_width, label='Total shots on target', color='#DB0000ff')
ax[0, 0].bar([i + 2*bar_width for i in indexes], df_arsenal_shots_accuracy['TGS'], width=bar_width, label='Total goals scored', color='#9C824A')
ax[0, 0].set_title('Arsenal')

ax[0, 1].bar(indexes, df_chelsea_shots_accuracy['HS'], width=bar_width, label='Total shots', color='#153D8A')
ax[0, 1].bar([i + bar_width for i in indexes], df_chelsea_shots_accuracy['HST'], width=bar_width, label='Total shots on target', color='#728AB9')
ax[0, 1].bar([i + 2*bar_width for i in indexes], df_chelsea_shots_accuracy['TGS'], width=bar_width, label='Total goals scored', color='#E30613')
ax[0, 1].set_title('Chelsea')

ax[0, 2].bar(indexes, df_liverpool_shots_accuracy['HS'], width=bar_width, label='Total shots', color='#610C0D')
ax[0, 2].bar([i + bar_width for i in indexes], df_liverpool_shots_accuracy['HST'], width=bar_width, label='Total shots on target', color='#00967F')
ax[0, 2].bar([i + 2*bar_width for i in indexes], df_liverpool_shots_accuracy['TGS'], width=bar_width, label='Total goals scored', color='#FEE942')
ax[0, 2].set_title('Liverpool')

ax[1, 0].bar(indexes, df_man_city_shots_accuracy['HS'], width=bar_width, label='Total shots', color='#002A5A')
ax[1, 0].bar([i + bar_width for i in indexes], df_man_city_shots_accuracy['HST'], width=bar_width, label='Total shots on target', color='#7AB2E1')
ax[1, 0].bar([i + 2*bar_width for i in indexes], df_man_city_shots_accuracy['TGS'], width=bar_width, label='Total goals scored', color='#DAA500')
ax[1, 0].set_title('Man City')

ax[1, 1].bar(indexes, df_man_united_shots_accuracy['HS'], width=bar_width, label='Total shots', color='#DA020E')
ax[1, 1].bar([i + bar_width for i in indexes], df_man_united_shots_accuracy['HST'], width=bar_width, label='Total shots on target', color='#FFE500')
ax[1, 1].bar([i + 2*bar_width for i in indexes], df_man_united_shots_accuracy['TGS'], width=bar_width, label='Total goals scored', color='#000000')
ax[1, 1].set_title('Man United')

ax[1, 2].bar(indexes, df_tottenham_shots_accuracy['HS'], width=bar_width, label='Total shots', color='#131F53')
ax[1, 2].bar([i + bar_width for i in indexes], df_tottenham_shots_accuracy['HST'], width=bar_width, label='Total shots on target', color='#dcdddc')
ax[1, 2].bar([i + 2*bar_width for i in indexes], df_tottenham_shots_accuracy['TGS'], width=bar_width, label='Total goals scored', color='#8a7470')
ax[1, 2].set_title('Tottenham')

for i in range(2):
    for j in range(3):
        ax[i, j].set_xticks([k + bar_width for k in np.arange(0, 5, 2)], df_filtered('Arsenal').loc[np.arange(0, 6, 2, dtype=int), 'Season'])
        ax[i, j].set_yticks(np.arange(50, 356, 100), minor=True)
        ax[i, j].set_ylim(0, 400)
        ax[i, j].tick_params(axis='both', labelsize=8)

plt.savefig('plots/big_six_shots_1.png')
plt.show()