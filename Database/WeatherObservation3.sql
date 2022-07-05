-- Query a list of CITY names from STATION for cities that have an even ID number. 
-- Print the results in any order, but exclude duplicates from the answer.

-- DBMS used: MySQL

select distinct(city) from station where id % 2 = 0;

-- or 

select distinct(city) from station where mod(id,2) = 0;

--mod is a function that returns the remainder of a division.