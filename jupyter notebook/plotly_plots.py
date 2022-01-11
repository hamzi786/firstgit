
import pandas as pd
chilla=pd.read_csv("data_chilla2.csv")
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

fig = px.scatter(data_frame=None, x="Gender", y="Location",
	         size="pop", color="continent",
                 hover_name="Purpose_for_chilla", log_x=True, size_max=60)
fig.show()