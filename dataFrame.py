import pandas as pd
import plotly.express as pe
data = [["pets", "animals"],["cat", "dog"]]
df = pd.DataFrame(data)
print(df)
df = pd.read_csv("line_chart.csv")
diagram = pe.line(df,x = "Year", y = "Per capita income", color = "Country", title = "Per Capita income per year in different countries")
diagram.show()