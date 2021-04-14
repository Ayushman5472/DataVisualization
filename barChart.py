import pandas as pd
import plotly.express as pe
df = pd.read_csv("data.csv")
diagram = pe.bar(df, x = "Country", y = "InternetUsers", title = "Internet Users in Countries")
diagram.show()