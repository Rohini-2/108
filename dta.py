import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv("data1.csv")
rating=df["Avg Rating"].tolist()
figure=ff.create_distplot([rating],["Avg Rating"],show_hist=False)
figure.show()