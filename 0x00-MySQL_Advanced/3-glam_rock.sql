-- SQL Script to list all Glam rock bands ranked by their longevity
-- scriot to list alll bands

SELECT 
    band_name, 
    CASE 
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM 
    metal_bands
WHERE 
    main_style = 'Glam rock'
ORDER BY 
    lifespan DESC;
