import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

df_chelsea_per_season = df_filtered('Chelsea')

plt.bar(df_chelsea_per_season['Season'], df_chelsea_per_season['TGS'], label='Total goals scored', color='#034696')
plt.bar(df_chelsea_per_season['Season'], df_chelsea_per_season['TGC'], label='Total goals conceded', color='#E3B841')
plt.title('Chelsea goals per season')
plt.xlabel('Seasons')
plt.ylabel('Goals')
plt.xticks(df_chelsea_per_season.loc[np.linspace(0, len(df_chelsea_per_season)-1, 6, dtype=int), 'Season'])
plt.yticks(np.arange(10, 111, 10), minor=True)
plt.legend(loc='lower right')
plt.savefig('plots/chelsea_goals_per_season.png')
plt.show()