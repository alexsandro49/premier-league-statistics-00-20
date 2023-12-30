import matplotlib.pyplot as plt
from main import df_filtered

df_chelsea_match_results = df_filtered('Chelsea')

plt.pie(df_chelsea_match_results, autopct='%1.1f%%', 
        pctdistance=0.85, colors=['#E30613', '#728AB9', '#153D8A'], 
        wedgeprops = {'linewidth' : 4, 'edgecolor' : 'white' }, 
        textprops = {'color': 'white', 'fontweight': 'bold'})
circle = plt.Circle((0,0), 0.7, color='white')
figure = plt.gcf()
figure.gca().add_artist(circle)

plt.title('Chelsea match results')
plt.legend(labels=[f'DEFEATS: {df_chelsea_match_results["DF"]}', 
        f'DRAWS: {df_chelsea_match_results["DW"]}', 
        f'WINNERS: {df_chelsea_match_results["WS"]}'], 
        loc='lower right', bbox_to_anchor=(1, -0.12))
plt.savefig('plots/chelsea_match_results.png')
plt.show()