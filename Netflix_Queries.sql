use netflix_db;
SELECT * FROM netflix_db.netflix_dataset;

-- Total titles 
SELECT COUNT(*) AS TotalTitles FROM netflix_dataset;

-- --Titles per Genre  
SELECT genre, COUNT(*) AS TotalTitles
FROM netflix_dataset
GROUP BY genre
ORDER BY TotalTitles DESC;

-- titles per Country 
SELECT country, COUNT(*) AS TotalTitles
FROM netflix_dataset
GROUP BY country
ORDER BY TotalTitles DESC;

-- Actual vs Forecast

SELECT release_year, COUNT(*) AS Titles, 'Actual' AS Type
FROM netflix_dataset
GROUP BY release_year
UNION
SELECT release_year, predicted_titles AS Titles, 'Forecast' AS Type
FROM netflix_forecast
ORDER BY release_year;
