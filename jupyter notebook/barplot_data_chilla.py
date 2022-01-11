import pandas as pd
chilla=pd.read_csv("data_chilla2.csv")

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

sns.barplot(x="Age", y='How many hours you code a day? (int) e.g: 5,4,3', hue="Location", data=chilla, color="blue", palette="pastel", saturation=1, dodge=True,  )
plt.show()