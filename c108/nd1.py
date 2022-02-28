import pandas as pd 
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")
weightList = df["Weight(Pounds)"].to_list()
figure = ff.create_distplot([weightList],["weightList"],show_hist = False)
figure.show()