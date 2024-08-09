-- SQL Script to rank country origins of bands by the number
-- This script aggregates the number of fans per country origin

SELECT 
    origin, 
    SUM(nb_fans) AS nb_fans
FROM 
    metal_bands
GROUP BY 
    origin
