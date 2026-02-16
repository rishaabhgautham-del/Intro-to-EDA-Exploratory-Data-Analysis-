import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing a dataset
df = pd.read_csv("Unicorn_Companies.csv")

#Inspecting the first 10 rows
first_10 = df.head(10)

#The size and shape of the dataset
size = df.size #Calculates the number of elements in the dataset
shape = df.shape #Returns a tuple in the (rows, columns) format

#Other information about the dataset
info = df.info()
