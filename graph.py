import pandas as pd
df=pd.read_csv("fianl_data.csv")
df.head()
df.columns
mass=df['mass'].to_list()
radius=df['radius'].to_list()
gravity=[]
def converttosi(radius,mass):
  for i in range(0,len(radius)-1):
    radius[i]=radius[i]* 6.957e+8
    mass[i]=mass[i]* 1.989e+30
converttosi(radius,mass)
def gravitycal(radius,mass):
  G=6.674e-11
  for i in range(0,len(mass)-1):
    g=(mass[index]*G)/((radius[index])**2)
    gravity.append(g)
    
gravitycal(radius,mass)
df["Gravity"]=gravity
df.to_csv("star_with_gravity.csv")
df.dtypes
