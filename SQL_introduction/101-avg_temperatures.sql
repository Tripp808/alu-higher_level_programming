USE hbtn_0c_0;

SELECT city, AVG((temperature * 9/5) + 32) AS avg_temp
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;
