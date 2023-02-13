import streamlit as st 
import pandas as pd
data=pd.read_csv("gapminder_with_code.CSV")
#read data from specific time
data_2007=data[data["year"]==2007]
data_2007

import matplotlib.pyplot as plt  

import numpy as np
import seaborn as sns

sns.set_theme()
# Create a random dataset across several variables
rs = np.random.default_rng(0)
n, p = 40, 8
d = rs.normal(0, 2, (n, p))
d += np.log(np.arange(1, p + 1)) * -5 + 10
# Show each distribution with both violins and points
var_x=[]
var_x.append(data["lifeExp"])

sns.violinplot(data=var_x, palette="light:g", inner="box", orient="h")


sns.set_theme()
# Create a random dataset across several variables
rs = np.random.default_rng(0)
n, p = 40, 8
d = rs.normal(0, 2, (n, p))
d += np.log(np.arange(1, p + 1)) * -5 + 10
# Show each distribution with both violins and points
var_x=[]
var_x.append(data["pop"])

sns.violinplot(data=var_x, palette="light:g", inner="box", orient="h")


sns.set_theme()
# Create a random dataset across several variables
rs = np.random.default_rng(0)
n, p = 40, 8
d = rs.normal(0, 2, (n, p))
d += np.log(np.arange(1, p + 1)) * -5 + 10
# Show each distribution with both violins and points
var_x=[]
var_x.append(data["lifeExp"])

sns.violinplot(data=var_x, palette="light:g", inner="box", orient="h")
