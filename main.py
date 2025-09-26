import psycopg2

db_config = {
    "host": "localhost",
    "database": "international_airport",
    "user": "tajwararik",
    "password": "137950",
    "port": 5432
}

def clean_sql(sql_text: str):
    """Remove comments and return cleaned SQL string."""
    lines = []
    for line in sql_text.splitlines():
        line = line.strip()
        if line.startswith("--") or line == "":
            continue
        lines.append(line)
    return " ".join(lines)

try:
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    print("✅ Connected to the database")

    # Read queries from file
    with open("queries.sql", "r", encoding="utf-8") as f:
        sql_script = f.read()

    # Clean and split queries
    cleaned_sql = clean_sql(sql_script)
    queries = [q.strip() for q in cleaned_sql.split(";") if q.strip()]

    for query in queries:
        cur.execute(query)

        if query.lower().startswith("select"):
            rows = cur.fetchall()
            print(f"\n📊 Results for query:\n{query}")
            for row in rows:
                print(row)

    conn.commit()
    print("\n✅ queries.sql executed successfully")

    cur.close()
    conn.close()
    print("🔒 Connection closed")

except Exception as e:
    print("❌ Error:", e)
