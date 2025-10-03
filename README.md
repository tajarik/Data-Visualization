# AeroInsight Analytics — International Airport Analytics

**Company:** AeroInsight Analytics

---

## Project overview

AeroInsight Analytics is a small analytics team embedded with a fictional international airport operator. This repository contains a relational dataset and analytical queries that explore passenger behavior, flight performance, baggage statistics, security outcomes, and airline/airport-level revenue. The goal is to practice joins, aggregations, time-series trends, and basic KPIs useful for airport operations and business intelligence.

Core analytics types: operational (on-time performance, security fails), commercial (revenue per airline, average ticket price), customer (baggage weight per passenger, passenger counts by country), and infrastructure (busiest airports/gates).

---

## Schema (high level)

The database is `international_airport` (Postgres). Key tables:

- `airline` — airline master data
- `airport` — airports (name, city, country)
- `flights` — flights with departure/arrival airport IDs and airline
- `booking` — bookings (price, platform, passenger_id)
- `booking_flight` — mapping bookings to flights (N-to-N)
- `passengers` — passenger demographics
- `boarding_pass` — boarding pass records (seat, boarding_time)
- `baggage` — baggage records (weight, booking_id)
- `baggage_check` — baggage security checks
- `security_check` — passenger security checks

Primary keys and foreign keys were created (see `schema.sql` / `dump.sql`).

---

## How to run (local development)

**Prerequisites**: PostgreSQL installed and running, Python 3.8+, git.

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/AeroInsight-Airport-Analytics.git
cd AeroInsight-Airport-Analytics
```

2. Create the Postgres database and import schema/data (adjust user/paths):

```bash
createdb international_airport
psql -U <db_user> -d international_airport -f schema.sql
# or if you have a full dump with data:
psql -U <db_user> -d international_airport -f dump.sql
```

3. Configure DB credentials: set environment variables or create a `config.py` / `.env` file. Example environment variables:

```bash
export DB_HOST=localhost
export DB_NAME=international_airport
export DB_USER=your_db_user
export DB_PASSWORD=your_password
export DB_PORT=5432
```

(Windows PowerShell: `$env:DB_PASSWORD = "your_password"`)

4. Run the query runner (example):

```bash
python main.py
# or a dedicated runner that formats SELECT results
python run_queries.py
```

---

## ER Diagram

![RED](diagram/ERD.png)

---
