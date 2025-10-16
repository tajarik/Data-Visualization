import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from config import DB_CONFIG

# Make sure charts/ exists
CHARTS_DIR = "charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

# Create DB engine
engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

def run_query(query: str):
    """Run SQL query and return dataframe"""
    return pd.read_sql(query, engine)

def save_and_report(fig, filename, df, description):
    """Save chart and print summary"""
    path = os.path.join(CHARTS_DIR, filename)
    fig.savefig(path, bbox_inches="tight")
    print(f"✅ {filename} saved. Rows: {len(df)}. {description}")
