import pandas as PD
import plotly.figure_factory as FF
import csv

df = PD.read_csv("data.csv")
fig = FF.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"])
fig.show()