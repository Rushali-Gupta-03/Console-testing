import plotly.graph_objects as go

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create the figure
fig = go.Figure()

# Add a trace (line plot)
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='lines+markers',
    name='Prime numbers',
    line=dict(color='blue'),
    marker=dict(size=8)
))

# Customize layout
fig.update_layout(
    title='Interactive Line Plot with Plotly',
    xaxis_title='X-axis',
    yaxis_title='Y-axis',
    showlegend=True
)

# Show the figure
# fig.show()
wd.save_graph(fig)