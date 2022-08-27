import pandas as pd
import csv

df = pd.read_csv("final.csv")
print(df.shape)

del df["Luminosity"]
del df["Unnamed: 0"]
print(df.shape)

df.to_csv("main.csv")