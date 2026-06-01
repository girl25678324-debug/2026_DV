import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Generate data
np.random.seed(42)
months = pd.date_range('2024-01-01', '2024-12-31', freq='ME')

df = pd.DataFrame({
    'month': months,
    'revenue': np.cumsum(np.random.uniform(80000, 120000, 12)),
    'customers': np.cumsum(np.random.randint(50, 150, 12)),
    'satisfaction': np.random.uniform(4.0, 4.8, 12)
})

# Create complex dashboard
fig = make_subplots(
    rows=4, cols=3,
    row_heights=[0.15, 0.35, 0.35, 0.15],
    column_widths=[0.33, 0.33, 0.34],
    specs=[
        [{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}],
        [{'type': 'scatter', 'colspan': 2}, None, {'type': 'bar'}],
        [{'type': 'scatter', 'colspan': 2}, None, {'type': 'pie'}],
        [{'type': 'table', 'colspan': 3}, None, None]
    ],
    subplot_titles=['', '', '',
                    'Revenue Growth Trend', '', 'Top Products',
                    'Customer Acquisition', '', 'Channel Mix',
                    ''],
    vertical_spacing=0.08,
    horizontal_spacing=0.05
)

# Row 1: KPI Indicators
fig.add_trace(go.Indicator(
    mode='number+delta',
    value=df['revenue'].iloc[-1],
    delta={'reference': df['revenue'].iloc[-2], 'relative': True, 'valueformat': '.1%'},
    title={'text': 'Monthly Revenue'},
    number={'prefix': '$', 'valueformat': ',.0f'},
    domain={'x': [0, 1], 'y': [0, 1]}
), row=1, col=1)

fig.add_trace(go.Indicator(
    mode='number+delta',
    value=df['customers'].iloc[-1],
    delta={'reference': df['customers'].iloc[-2], 'relative': True, 'valueformat': '.1%'},
    title={'text': 'Total Customers'},
    number={'valueformat': ','},
    domain={'x': [0, 1], 'y': [0, 1]}
), row=1, col=2)

fig.add_trace(go.Indicator(
    mode='gauge+number+delta',
    value=df['satisfaction'].iloc[-1],
    delta={'reference': 4.0},
    gauge={'axis': {'range': [1, 5]},
           'bar': {'color': '#06A77D'},
           'threshold': {'line': {'color': 'red', 'width': 4},
                        'thickness': 0.75, 'value': 4.0}},
    title={'text': 'Satisfaction'},
    domain={'x': [0, 1], 'y': [0, 1]}
), row=1, col=3)

# Row 2: Revenue trend and Top Products
fig.add_trace(go.Scatter(
    x=df['month'], y=df['revenue'],
    mode='lines+markers',
    line=dict(color='#2E86AB', width=3),
    fill='tozeroy',
    fillcolor='rgba(46, 134, 171, 0.2)',
    name='Revenue'
), row=2, col=1)

products = ['Product A', 'Product B', 'Product C', 'Product D']
product_sales = [450000, 380000, 320000, 280000]
fig.add_trace(go.Bar(
    x=product_sales, y=products,
    orientation='h',
    marker_color='#FF6B6B',
    name='Sales'
), row=2, col=3)

# Row 3: Customer acquisition and Channel mix
fig.add_trace(go.Scatter(
    x=df['month'], y=df['customers'],
    mode='lines+markers',
    line=dict(color='#06A77D', width=3),
    name='Customers'
), row=3, col=1)

channels = ['Direct', 'Partner', 'Online', 'Reseller']
channel_revenue = [35, 28, 22, 15]
fig.add_trace(go.Pie(
    labels=channels, values=channel_revenue,
    marker_colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'],
    name='Channels'
), row=3, col=3)

# Row 4: Summary table
fig.add_trace(go.Table(
    header=dict(values=['<b>Metric</b>', '<b>Current</b>', '<b>Target</b>', '<b>Status</b>'],
                fill_color='#2E86AB',
                font=dict(color='white', size=12),
                align='left'),
    cells=dict(values=[
        ['Revenue', 'Customers', 'Profit Margin', 'Satisfaction'],
        ['$1.18M', '4,850', '28%', '4.5/5'],
        ['$1.10M', '4,500', '25%', '4.0/5'],
        [' Exceeds', ' Exceeds', ' Exceeds', ' Exceeds']
    ],
    fill_color=[['#F8F9FA', 'white']*4],
    font=dict(size=11),
    align='left')
), row=4, col=1)

# Update layout
fig.update_layout(
    title_text='<b>Executive Dashboard - December 2024</b><br>' +
               '<sub>Key metrics and performance indicators</sub>',
    title_x=0.5,
    title_y=0.98,
    title_font_size=22,
    showlegend=False,
    height=1200,
    plot_bgcolor='#F8F9FA',
    paper_bgcolor='white'
)

# Format axes
fig.update_xaxes(showgrid=True, gridcolor='white')
fig.update_yaxes(showgrid=True, gridcolor='white')

fig.show()
