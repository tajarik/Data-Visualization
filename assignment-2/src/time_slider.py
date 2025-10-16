import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from config import DB_CONFIG

# --- Database connection ---
engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

# --- SQL query for monthly bookings ---
TIMESLIDER_BAR = """
SELECT DATE_TRUNC('month', b.created_at) AS month,
       COUNT(*) AS total_bookings
FROM booking b
GROUP BY month
ORDER BY month;
"""

df = pd.read_sql(TIMESLIDER_BAR, engine)

# Format month
df['month'] = pd.to_datetime(df['month'])
df = df.sort_values('month')

# Add cumulative
df['cumulative_bookings'] = df['total_bookings'].cumsum()
df['month_str'] = df['month'].dt.strftime('%Y-%m')

# --- Build expanding dataset for animation ---
frames = []
for i in range(len(df)):
    subset = df.iloc[:i+1].copy()
    subset['frame'] = df.iloc[i]['month_str']
    frames.append(subset)
df_expanded = pd.concat(frames)

# --- Plotly cumulative bar chart ---
fig = px.bar(
    df_expanded,
    x="cumulative_bookings",
    y="month_str",
    orientation="h",
    animation_frame="frame",
    range_x=[0, df['cumulative_bookings'].max() + 10],
    title="📅 Cumulative Monthly Booking Trends (Animated)"
)

fig.show()
