# Pie chart: On-time vs Delayed flights
PIE_FLIGHTS = """
SELECT 
    CASE 
        WHEN f.actual_departure <= f.scheduled_departure THEN 'On Time'
        ELSE 'Delayed'
    END AS departure_status,
    COUNT(*) AS total_flights
FROM flights f
JOIN airline a ON f.airline_id = a.airline_id
GROUP BY departure_status;
"""

# Bar chart: Top 5 airlines by revenue
BAR_REVENUE = """
SELECT al.airline_name, SUM(bk.price) AS total_revenue
FROM booking bk
JOIN booking_flight bf ON bk.booking_id = bf.booking_id
JOIN flights f ON bf.flight_id = f.flight_id
JOIN airline al ON f.airline_id = al.airline_id
GROUP BY al.airline_name
ORDER BY total_revenue DESC
LIMIT 5;
"""

# Horizontal bar: Bookings per platform
HORIZONTAL_PLATFORM = """
SELECT b.booking_platform, COUNT(*) AS total_bookings
FROM booking b
JOIN passengers p ON b.passenger_id = p.passenger_id
GROUP BY b.booking_platform
ORDER BY total_bookings DESC
LIMIT 10;
"""

# Line chart: Monthly booking trends
LINE_BOOKINGS = """
SELECT DATE_TRUNC('month', b.created_at) AS month, COUNT(*) AS total_bookings
FROM booking b
JOIN passengers p ON b.passenger_id = p.passenger_id
GROUP BY month
ORDER BY month;
"""

# Histogram: Baggage weights
HIST_BAGGAGE = """
SELECT b.weight_in_kg
FROM baggage b
JOIN booking bk ON b.booking_id = bk.booking_id
JOIN passengers p ON bk.passenger_id = p.passenger_id;
"""

# Scatter plot: Ticket price vs Baggage weight
SCATTER_PRICE_BAGGAGE = """
SELECT bk.price, b.weight_in_kg
FROM booking bk
JOIN baggage b ON bk.booking_id = b.booking_id
JOIN passengers p ON bk.passenger_id = p.passenger_id;
"""
