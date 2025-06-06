select count(*) from cohort_table;


-- first 5 rows
SELECT * FROM cohort_Table
LIMIT 5;


-- info
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'COHORT_TABLE';


-- mean, median
SELECT
  AVG(quantity) AS mean,
  MIN(quantity) AS minimum,
  MAX(quantity) AS maximum,
  STDDEV(quantity) AS std_dev,
  COUNT(quantity) AS total_count
FROM cohort_table;


-- null and missing values
SELECT
  COUNT(*) FILTER (WHERE cohort_code IS NULL) AS null_in_cohort_code,
  COUNT(*) FILTER (WHERE quantity IS NULL) AS null_in_quantity
FROM cohort_table;


SELECT cohort_code, COUNT(*) 
FROM cohort_table
GROUP BY cohort_code
HAVING COUNT(*) > 1;
