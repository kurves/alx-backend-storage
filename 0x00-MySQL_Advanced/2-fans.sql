-- SQL Script to rank country origins of bands by the number of (non-unique) fans
-- This script aggregates the number of fans per country origin and orders the result in descending order of fans.

SELECT 
    origin, 
    SUM(nb_fans) AS nb_fans
FROM 
    metal_bands
GROUP BY 
    origin
ORDER BY 
    nb_fans DESC;
