import pandas as pd
from pandas.core.frame import DataFrame
chilla=pd.read_csv("data_chilla2.csv")
print(chilla)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

sns.countplot(x="Gender", hue="Location", data=chilla, color="blue", palette="pastel", saturation=1, dodge=True, )
plt.show()