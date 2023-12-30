import matplotlib.pyplot as plt
from main import df_filtered

teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Man United', 'Tottenham']
df_big_six_match_results = [df_filtered(i) for i in teams]

fig, ax = plt.subplots(2, 3, figsize=(8, 5))
fig.suptitle('Bix six match results')
plt.subplots_adjust(hspace=0.4)

count = 0
for i in range(2):
    for j in range(3):
        ax[i, j].set_title(teams[count])
        ax[i, j].pie(df_big_six_match_results[count], colors=['#DB0000ff', '#00967F','#002A74ff'], 
        wedgeprops = {'linewidth' : 4, 'edgecolor' : 'white' }, 
        textprops = {'color': 'white', 'fontweight': 'bold'})
        count += 1

plt.legend(labels=['DEFEATS', 'DRAWS', 'WINNERS'], loc='lower left', ncols=3, bbox_to_anchor=(-2, -0.2))
plt.savefig('plots/big_six_results_1.png')
plt.show()