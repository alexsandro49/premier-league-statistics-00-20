import numpy as np
import matplotlib.pyplot as plt
from main import df_filtered

df_liverpool_per_season = df_filtered('Liverpool')

plt.bar(df_liverpool_per_season['Season'], df_liverpool_per_season['TGS'], label='Total goals scored', color='#00967F')
plt.bar(df_liverpool_per_season['Season'], df_liverpool_per_season['TGC'], label='Total goals conceded', color='#610C0D')
plt.title('Liverpool goals by season')
plt.xlabel('Seasons')
plt.ylabel('Goals')
plt.ylim(0, 130)
plt.xticks(df_liverpool_per_season.loc[np.linspace(0, len(df_liverpool_per_season)-1, 6, dtype=int), 'Season'])
plt.yticks(np.arange(10, 131, 20), minor=True)
plt.legend(loc='upper center', ncols=2, fontsize=9)
plt.savefig('plots/liverpool_goals_by_season.png')
plt.show()