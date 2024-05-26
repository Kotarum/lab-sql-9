-- Create a table `rentals_may` to store data for May:
CREATE TABLE rentals_may AS
SELECT *
FROM rental
WHERE MONTH(rental_date) = 5;

-- Create a table `rentals_june` to store data for June:
CREATE TABLE rentals_june AS
SELECT *
FROM rental
WHERE MONTH(rental_date) = 6;

-- Check the number of rentals for each customer for May:
SELECT customer_id, COUNT(*) AS may_rentals
FROM rentals_may
GROUP BY customer_id;

-- Check the number of rentals for each customer for June:
SELECT customer_id, COUNT(*) AS june_rentals
FROM rentals_june
GROUP BY customer_id;