import pandas as pd
import csv

df = pd.read_csv("bright_stars.csv")
del df["Luminosity"]
df.to_csv('project.csv') 