import pandas as ps 
import plotly.express as px
df = ps.read_csv("COVID.csv")
fig = px.scatter(df, x = 'date', y = 'cases', color = 'country', size_max = 30)
fig.show()