import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Create narrative report structure
fig = make_subplots(
    rows=5, cols=1,
    row_heights=[0.1, 0.25, 0.25, 0.25, 0.15],
    specs=[
        [{'type': 'table'}],
        [{'type': 'scatter'}],
        [{'type': 'bar'}],
        [{'type': 'scatter'}],
        [{'type': 'table'}]
    ],
    subplot_titles=['',
                    '1. Revenue Shows Strong Growth Throughout 2024',
                    '2. Regional Performance Varies Significantly',
                    '3. Customer Satisfaction Remains High Despite Growth',
                    ''],
    vertical_spacing=0.08
)

# Executive Summary (top)
fig.add_trace(go.Table(
    header=dict(values=['<b>Executive Summary: 2024 Performance Review</b>'],
                fill_color='#2E86AB',
                font=dict(color='white', size=14),
                height=40),
    cells=dict(values=[
        ['Our analysis reveals strong growth in 2024 with revenue increasing 45% YoY. ' +
         'Regional performance shows East region leading growth at 52%, while South lags at 28%. ' +
         'Customer satisfaction remained consistently above 4.5/5 despite rapid scaling. ' +
         'Recommendations: Invest in South region training, maintain quality focus during growth.']
    ],
    fill_color='#F8F9FA',
    font=dict(size=12),
    height=30,
    align='left')
), row=1, col=1)

# Chart 1: Revenue trend with annotations
months = pd.date_range('2024-01-01', '2024-12-31', freq='ME')
revenue = np.cumsum(np.random.uniform(80000, 120000, 12))

fig.add_trace(go.Scatter(
    x=months, y=revenue,
    mode='lines+markers',
    line=dict(color='#2E86AB', width=3),
    name='Revenue'
), row=2, col=1)

# Add annotation for key insight
fig.add_annotation(
    x=months[8], y=revenue[8],
    text='Q3 surge due to<br>new product launch',
    showarrow=True,
    arrowhead=2,
    ax=-50, ay=-50,
    row=2, col=1
)

# Chart 2: Regional comparison
regions = ['North', 'South', 'East', 'West']
growth = [42, 28, 52, 38]
fig.add_trace(go.Bar(
    x=regions, y=growth,
    marker_color=['#06A77D' if g > 40 else '#FFA07A' for g in growth],
    text=[f'{g}%' for g in growth],
    textposition='outside'
), row=3, col=1)

# Chart 3: Satisfaction trend
satisfaction = np.random.uniform(4.3, 4.7, 12)
fig.add_trace(go.Scatter(
    x=months, y=satisfaction,
    mode='lines+markers',
    line=dict(color='#06A77D', width=3)
), row=4, col=1)

# Add target line (use add_shape for compatibility with mixed subplot types)
fig.add_shape(type='line', x0=0, x1=1, xref='x4 domain',
              y0=4.0, y1=4.0, yref='y4',
              line=dict(dash='dash', color='red'))
fig.add_annotation(x=0.5, xref='x4 domain', y=4.0, yref='y4',
                   text='Minimum Target', showarrow=False, yshift=12)

# Recommendations (bottom)
fig.add_trace(go.Table(
    header=dict(values=['<b>Strategic Recommendations</b>'],
                fill_color='#06A77D',
                font=dict(color='white', size=14)),
    cells=dict(values=[
        ['1. South Region: Deploy best practices from East region, provide additional training<br>' +
         '2. Scaling: Maintain quality controls as customer base grows, hire support staff<br>' +
         '3. Products: Capitalize on Q3 success, plan Q2 2025 launch<br>' +
         '4. Investment: Allocate additional budget to high-growth regions']
    ],
    fill_color='#F8F9FA',
    font=dict(size=11),
    align='left')
), row=5, col=1)

fig.update_layout(
    title='<b>2024 Annual Performance Analysis</b><br>' +
          '<sub>Prepared for Executive Leadership Team | January 2025</sub>',
    title_x=0.5,
    title_font_size=20,
    showlegend=False,
    height=1400,
    plot_bgcolor='white',
    paper_bgcolor='white'
)

fig.show()
fig.write_html(
    'Executive_Dashboard_Dec2024.html',
    config={
        'displayModeBar': True,  # Show toolbar
        'displaylogo': False,    # Remove Plotly logo
        'modeBarButtonsToRemove': ['lasso2d', 'select2d']  # Remove unnecessary buttons
    }
)
fig.write_image(
    'Dashboard_Report.png',
    width=1920,
    height=1080,
    scale=2  # High resolution
)
