
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Console.package import Functions


f = Functions()

# your code here
np.random.seed(10)
data = np.random.normal(100, 20, 200)
 
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
fig= plt.boxplot(data)
 
# show plot
f.save_image(plt)
