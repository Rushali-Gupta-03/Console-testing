!pip install -r requirements.txt
from warpdrive import WarpDrive
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from catboost import CatBoostClassifier

#comment

wd = WarpDrive()

df = wd.get_args("df")
mod = wd.get_args("mod")
strr = wd.get_args("strr")
csv = wd.get_args("csv")
cols = wd.get_args("col")
# your code here
df1 = pd.read_csv('consolefiles/csv.csv')
wd.save_table(df)
wd.save_table(df1)
wd.save_table(cols)
wd.create_df(df)
exog_columns = ["Loan_Amount", "Home_Owner"]

# Train the CatBoostClassifier only on the exogenous columns
clf = CatBoostClassifier(random_state=0).fit(df[exog_columns].values, df['Gender'].values)

# Update col to reflect that only exog_columns are used
col = exog_columns

# Create the model using the specified exogenous columns
wd.create_model(
    model=clf,
    library="catboost",
    model_technique="CatBoostClassifier",
    input_variables=col,  # Only exogenous columns are used
    target_column="Gender",
    train_table="df",
    lags=0,
    exog_columns=exog_columns,
)

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot
plt.plot(x, y, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Show grid
plt.grid(True)
wd.save_image(plt)
# Show plot
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Create a bar trace
trace = go.Bar(x=categories, y=values)

# Create the layout
layout = go.Layout(title='Bar Chart Example', xaxis=dict(title='Categories'), yaxis=dict(title='Values'))

# Create the figure
fig = go.Figure(data=[trace], layout=layout)
wd.save_graph(fig)
# Display the figure