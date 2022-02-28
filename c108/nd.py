import pandas as pd 
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")
heightList = df["Height(Inches)"].to_list()
figure = ff.create_distplot([heightList],["heightList"],show_hist = False)
figure.show()