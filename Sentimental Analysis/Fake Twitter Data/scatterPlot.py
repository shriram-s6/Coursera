import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('resulting_data.csv')
retweet_count = data['Number of Retweets']
net_score = data['Net Score']
colors = data['Net Score']
plt.title('Sentimental Analysis Results')
plt.xlabel('Net Sentiment Score')
plt.ylabel('No of Retweets')
plt.tight_layout()
plt.scatter(net_score, retweet_count, s=50, c=colors, cmap='Greens'
            , edgecolors='b', linewidth=1, alpha=0.75)
plt.show()
