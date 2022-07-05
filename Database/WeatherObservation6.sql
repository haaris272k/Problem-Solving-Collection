-----NOTE--------------------------------------------------------------------------------

---[ Putting % af any char along with the 'LIKE' operator will return the required data 
--that starts with that char.]

--- [Putting % af before any char along with the 'LIKE' operator will return the required data
--- that ends with that char]

-----------------------------------------------------------------------------------------

-- (A) Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION.
--  Your result cannot contain duplicates.

select distinct(city) from station where 
city like 'a%' or city like 'e%' or city like 'o%' or city like 'i%' or city like 'u%'


--(B) Query the list of CITY names ending with vowels (i.e., a, e, i, o, or u) from STATION.
--  Your result cannot contain duplicates.

select distinct(city) from station where
city like '%a' or city like '%e' or city like '%o' or city like '%i' or city like '%u'