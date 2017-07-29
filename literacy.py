import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("/media/arvind/New Volume/daTAscience/Literacy_and_Literacy_Rate.csv")
#print(df.describe())

#comparing the literacy rate of males and females districtwise
plt.bar(range(len(df["Males"])),df["Literacy_Rate_Males"],color="blue",label="Males")
plt.bar(range(len(df["Females"])),df["Literacy_Rate_Females"],color="pink",label="Females")
plt.xlabel("Districts")
plt.ylabel("Literacy Rate")
plt.legend(loc="best")
plt.xticks(range(len(df["Females"])),df["Districts"], rotation="vertical")  #used to provide names for x axis values
plt.show()

# #number of males and females in a district
plt.bar(range(len(df["Males"])),(df["Males"]/df["Females"]),color="blue")
#plt.bar(range(len(df["Females"])),df["Females"],color="pink")
plt.xticks(range(len(df["Females"])),df["Districts"],rotation="vertical")
plt.show()
plt.show()
#read google file system (GFS) and mongoDB and mapreduce




