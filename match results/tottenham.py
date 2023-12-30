import matplotlib.pyplot as plt
from main import df_filtered

df_tottenham_match_results = df_filtered('Tottenham')

plt.pie(df_tottenham_match_results, autopct='%1.1f%%', 
        pctdistance=0.85, colors=['#dcdddc', '#8a7470','#001B57ff'], 
        wedgeprops = {'linewidth' : 4, 'edgecolor' : 'white' }, 
        textprops = {'color': 'white', 'fontweight': 'bold'})
circle = plt.Circle((0,0), 0.7, color='white')
figure = plt.gcf()
figure.gca().add_artist(circle)

plt.title('Tottenham match results')
plt.legend(labels=[f'DEFEATS: {df_tottenham_match_results["DF"]}', 
        f'DRAWS: {df_tottenham_match_results["DW"]}', 
        f'WINNERS: {df_tottenham_match_results["WS"]}'], 
        loc='lower right', bbox_to_anchor=(1, -0.12))
plt.savefig('plots/tottenham_match_results.png')
plt.show()