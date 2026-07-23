SELECT COUNT(*) AS total_city
FROM weather.dim_city;

SELECT COUNT(DISTINCT city_name)
FROM weather.dim_city;

SELECT MIN(latitude),
       MAX(latitude)
FROM weather.dim_city;