import pandas as pd
chilla=pd.read_csv("data_chilla2.csv")
import plotly as pt
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

sns.relplot(x="Gender", y="Age", hue="Location", size=2)
plt.show()