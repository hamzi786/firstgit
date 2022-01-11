import pandas as pd
chilla=pd.read_csv("data_chilla2.csv")

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

g=sns.FacetGrid(chilla, row="Gender", hue="field_of_study")
g=(g.map(plt.scatter, "Age", "Location").add_legend())
plt.show()