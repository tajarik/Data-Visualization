-- Check the first 10 passengers
SELECT * FROM passengers LIMIT 10;

-- Get flights departing after 2024-01-01, sorted by departure date (newest first)
SELECT * FROM flights 
WHERE scheduled_departure > '2024-01-01' 
ORDER BY scheduled_departure DESC LIMIT 10;

-- Analyze baggage patterns
SELECT 
    COUNT(baggage_id) as total_bags,
    AVG(weight_in_kg) as avg_weight,
    MIN(weight_in_kg) as min_weight,
    MAX(weight_in_kg) as max_weight
FROM baggage;

-- JOIN between passengers and their bookings
SELECT 
    p.passenger_id,
    p.first_name,
    p.last_name,
    b.booking_id
FROM passengers p
JOIN booking b ON p.passenger_id = b.passenger_id
LIMIT 10;

-- 1. Number of passengers per country of citizenship
SELECT country_of_citizenship, COUNT(*) AS total_passengers
FROM passengers
GROUP BY country_of_citizenship
ORDER BY total_passengers DESC LIMIT 5;

-- 2. Top 5 busiest airports by number of departing flights
SELECT a.airport_name, COUNT(f.flight_id) AS total_departures
FROM flights f
JOIN airport a ON f.departure_airport_id = a.airport_id
GROUP BY a.airport_name
ORDER BY total_departures DESC
LIMIT 5;

-- 3. Average baggage weight per passenger
SELECT p.passenger_id, p.first_name, p.last_name, AVG(b.weight_in_kg) AS avg_baggage_weight
FROM passengers p
JOIN booking bk ON p.passenger_id = bk.passenger_id
JOIN baggage b ON bk.booking_id = b.booking_id
GROUP BY p.passenger_id, p.first_name, p.last_name
ORDER BY avg_baggage_weight DESC LIMIT 5;

-- 4. Number of bookings per booking platform
SELECT booking_platform, COUNT(*) AS total_bookings
FROM booking
GROUP BY booking_platform
ORDER BY total_bookings DESC LIMIT 5;

-- 5. On-time vs delayed flights
SELECT 
    CASE 
        WHEN actual_departure <= scheduled_departure THEN 'On Time'
        ELSE 'Delayed'
    END AS departure_status,
    COUNT(*) AS total_flights
FROM flights
GROUP BY departure_status;

-- 6. Average ticket price by booking platform
SELECT booking_platform, AVG(price) AS avg_ticket_price
FROM booking
GROUP BY booking_platform
ORDER BY avg_ticket_price DESC LIMIT 5;

-- 7. Top 5 airlines by number of flights
SELECT al.airline_name, COUNT(f.flight_id) AS total_flights
FROM flights f
JOIN airline al ON f.airline_id = al.airline_id
GROUP BY al.airline_name
ORDER BY total_flights DESC
LIMIT 5;

-- 8. Passengers who failed security checks
SELECT p.passenger_id, p.first_name, p.last_name, sc.check_result
FROM passengers p
JOIN security_check sc ON p.passenger_id = sc.passenger_id
WHERE sc.check_result = 'Failed';

-- 9. Revenue generated per airline
SELECT al.airline_name, SUM(bk.price) AS total_revenue
FROM booking bk
JOIN booking_flight bf ON bk.booking_id = bf.booking_id
JOIN flights f ON bf.flight_id = f.flight_id
JOIN airline al ON f.airline_id = al.airline_id
GROUP BY al.airline_name
ORDER BY total_revenue DESC LIMIT 5;

-- 10. Monthly passenger booking trends
SELECT DATE_TRUNC('month', created_at) AS month, COUNT(*) AS total_bookings
FROM booking
GROUP BY month
ORDER BY month;

