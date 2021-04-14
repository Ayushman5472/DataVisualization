import pandas as pd
import plotly.express as pe
df = pd.read_csv("data.csv")
diagram = pe.scatter(df,x = "Population", y = "InternetUsers", color = "Country", title = "Internet users in countries", size = "Per capita")
diagram.show()