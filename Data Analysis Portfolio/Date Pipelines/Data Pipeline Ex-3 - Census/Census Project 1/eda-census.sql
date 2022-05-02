--Chapter 4 SQL Queries: Practical SQL 1st Edition
SELECT * FROM us_counties_2010;

-- 4-3: Using the copy command to import data to the database (census.csv)

COPY us_counties_2010
FROM '/Users/christophermarshall/Documents/Data Analysis Portfolio/Date Pipelines/census.csv'
WITH (FORMAT CSV, HEADER);

-- Running basic SELECT statements to explore data (Alaska has the largest counties by land area)

SELECT * FROM us_counties_2010;

SELECT geo_name, state_us_abbreviation, area_land
FROM us_counties_2010
ORDER BY area_land DESC
LIMIT 3;

SELECT geo_name, state_us_abbreviation, internal_point_lon
FROM us_counties_2010
ORDER BY internal_point_lon DESC
LIMIT 5;


-- Creating a new table to track supervisor salaries 

CREATE TABLE supervisor_salaries (
    town varchar(30),
    county varchar(30),
    supervisor varchar(30),
    start_date date,
    salary money,
    benefits money
);

-- Performaing a similar import (using copy command) from above to include additional salary data

COPY supervisor_salaries (town, supervisor, salary)
FROM '/Users/christophermarshall/Documents/Data Analysis Portfolio/Date Pipelines/salary.csv'
WITH (FORMAT CSV, HEADER);

-- Check the data
SELECT * FROM supervisor_salaries LIMIT 2;

-- Listing 4-6 Use a temporary table to add a default value to a column during
-- import

DELETE FROM supervisor_salaries;

CREATE TEMPORARY TABLE supervisor_salaries_temp (LIKE supervisor_salaries);

COPY supervisor_salaries_temp (town, supervisor, salary)
FROM '/Users/christophermarshall/Documents/Data Analysis Portfolio/Date Pipelines/salaries.csv'
WITH (FORMAT CSV, HEADER);

INSERT INTO supervisor_salaries (town, county, supervisor, salary)
SELECT town, 'Some County', supervisor, salary
FROM supervisor_salaries_temp;

DROP TABLE supervisor_salaries_temp;

-- Check the data
SELECT * FROM supervisor_salaries LIMIT 2;

-- Use the copy command to export table to file location

COPY us_counties_2010
TO '/Users/christophermarshall/Documents/Data Analysis Portfolio/Date Pipelines/census_export.txt'
WITH (FORMAT CSV, HEADER, DELIMITER '|');


-- You can also export just specific columns from a table with COPY

COPY us_counties_2010 (geo_name, internal_point_lat, internal_point_lon)
TO 'C:\YourDirectory\us_counties_latlon_export.txt'
WITH (FORMAT CSV, HEADER, DELIMITER '|');

-- You can also export query results with COPY

COPY (
    SELECT geo_name, state_us_abbreviation
    FROM us_counties_2010
    WHERE geo_name ILIKE '%mill%'
     )
TO 'C:\YourDirectory\us_counties_mill_export.txt'
WITH (FORMAT CSV, HEADER, DELIMITER '|');