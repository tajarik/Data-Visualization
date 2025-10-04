# src/demo.py

import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text
import os
from config import DB_CONFIG
import queries as q
from charts import run_query, save_and_report

# ------------------------
# Setup
# ------------------------
engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

CHARTS_DIR = "charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

# ------------------------
# Step 1 – Show scatter BEFORE insert
# ------------------------
print("📊 Generating scatter BEFORE insertion...\n")

df_before = run_query(q.SCATTER_PRICE_BAGGAGE)
fig1, ax1 = plt.subplots()
ax1.scatter(df_before['weight_in_kg'], df_before['price'], alpha=0.6, color="purple")
ax1.set_title("Ticket Price vs Baggage Weight (Before)")
ax1.set_xlabel("Baggage Weight (kg)")
ax1.set_ylabel("Ticket Price")
save_and_report(fig1, "scatter_before.png", df_before, "Scatter plot before insertion")

# ------------------------
# Step 2 – Insert new row
# ------------------------
print("\n📝 Inserting new baggage record...")

insert_sql = text("""
INSERT INTO baggage (baggage_id, booking_id, weight_in_kg)
VALUES ((SELECT COALESCE(MAX(baggage_id), 0) + 1 FROM baggage), 1, 95.0)
RETURNING baggage_id;
""")

new_id = None
try:
    with engine.begin() as conn:
        result = conn.execute(insert_sql)
        new_id = result.scalar()
    print(f"✅ Inserted new baggage with id={new_id}, weight=95.0kg, booking_id=1.")

    # ------------------------
    # Step 3 – Show scatter AFTER insert
    # ------------------------
    print("\n📊 Regenerating scatter AFTER insertion...\n")

    df_after = run_query(q.SCATTER_PRICE_BAGGAGE)
    fig2, ax2 = plt.subplots()

    # Original scatter
    ax2.scatter(df_after['weight_in_kg'], df_after['price'], alpha=0.6, color="purple")

    # Highlight the newly inserted baggage in RED
    new_row = df_after[df_after['weight_in_kg'] == 95.0]
    if not new_row.empty:
        ax2.scatter(new_row['weight_in_kg'], new_row['price'],
                    color="red", marker="x", s=120, label="New Row")

    ax2.set_title("Ticket Price vs Baggage Weight (After)")
    ax2.set_xlabel("Baggage Weight (kg)")
    ax2.set_ylabel("Ticket Price")
    ax2.legend()

    save_and_report(fig2, "scatter_after.png", df_after, "Scatter plot after insertion")

finally:
    # ------------------------
    # Step 4 – Rollback cleanup
    # ------------------------
    if new_id:
        with engine.begin() as conn:
            conn.execute(text("DELETE FROM baggage WHERE baggage_id = :id"), {"id": new_id})
        print(f"\n🧹 Cleanup: Deleted test baggage row with id={new_id}.")

print("\n🎉 Demo complete! Check /charts for before/after comparisons.")
