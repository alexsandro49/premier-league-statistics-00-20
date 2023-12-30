import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

df_man_united_per_season = df_filtered('Man United')

plt.bar(df_man_united_per_season['Season'], df_man_united_per_season['TGS'], label='Total goals scored', color='#DA020E')
plt.bar(df_man_united_per_season['Season'], df_man_united_per_season['TGC'], label='Total goals conceded', color='#FFE500')
plt.title('Man United goals by season')
plt.xlabel('Seasons')
plt.ylabel('Goals')
plt.ylim(0, 130)
plt.xticks(df_man_united_per_season.loc[np.linspace(0, len(df_man_united_per_season)-1, 6, dtype=int), 'Season'])
plt.yticks(np.arange(10, 131, 20), minor=True)
plt.legend(loc='upper center', ncols=2, fontsize=9)
plt.savefig('plots/man_united_goals_by_season.png')
plt.show()