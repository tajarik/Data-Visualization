import psycopg2
import random
import time
from datetime import date

# --- CONFIG ---
DB_NAME = "international_airport"
DB_USER = "tajwararik"
DB_PASS = "137950"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_random_id(cur, table, id_col):
    cur.execute(f"SELECT {id_col} FROM {table} ORDER BY RANDOM() LIMIT 1;")
    return cur.fetchone()[0]

def insert_booking():
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS,
        host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()

    passenger_id = get_random_id(cur, "passengers", "passenger_id")
    flight_id = get_random_id(cur, "flights", "flight_id")

    booking_platform = random.choice(["Expedia", "Booking.com", "FlyNow", "SkyJet", "AirWorld"])
    status = random.choice(["Confirmed", "Pending", "Cancelled"])
    price = round(random.uniform(100.0, 9000.0), 2)
    today = date.today()

    # --- Insert into booking ---
    cur.execute("""
        INSERT INTO booking (passenger_id, booking_platform, created_at, update_at, status, price)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING booking_id;
    """, (passenger_id, booking_platform, today, today, status, price))

    booking_id = cur.fetchone()[0]

    # --- Insert into booking_flight ---
    cur.execute("""
        INSERT INTO booking_flight (booking_id, flight_id, created_at, update_at)
        VALUES (%s, %s, %s, %s);
    """, (booking_id, flight_id, today, today))

    # --- Insert into baggage ---
    weight = round(random.uniform(5.0, 40.0), 2)
    cur.execute("""
        INSERT INTO baggage (weight_in_kg, created_date, update_date, booking_id)
        VALUES (%s, %s, %s, %s);
    """, (weight, today, today, booking_id))

    conn.commit()
    cur.close()
    conn.close()

    print(f"[+] Inserted booking_id={booking_id} | passenger_id={passenger_id} | flight_id={flight_id}")

if __name__ == "__main__":
    while True:
        insert_booking()
        time.sleep(10)  # every 10 seconds
