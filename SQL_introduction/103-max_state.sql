USE hbtn_0c_0;

SELECT state, MAX(temperature) AS max_temp
FROM temperature_data
GROUP BY state
ORDER BY state ASC;
