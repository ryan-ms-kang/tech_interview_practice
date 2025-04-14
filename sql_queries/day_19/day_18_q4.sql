/*
Amazon wants to maximize the storage capacity of its 500,000 square-foot warehouse by prioritizing a specific batch of prime items. 
The specific prime product batch detailed in the inventory table must be maintained.

So, if the prime product batch specified in the item_category column included 1 laptop and 1 side table, that would be the base batch.
 We could not add another laptop without also adding a side table; they come all together as a batch set.

After prioritizing the maximum number of prime batches, any remaining square footage will be utilized to stock non-prime batches, 
which also come in batch sets and cannot be separated into individual items.

Write a query to find the maximum number of prime and non-prime batches that can be stored in the 500,000 square feet warehouse 
based on the following criteria:

Prioritize stocking prime batches
After accommodating prime items, allocate any remaining space to non-prime batches
Output the item_type with prime_eligible first followed by not_prime, along with the maximum number of batches that can be stocked.
*/ 

WITH type_grouped AS (
  SELECT 
    item_type,
    SUM(square_footage) AS total_sqft_one_batch,
    COUNT(*) AS item_count
  FROM inventory
  GROUP BY 1
), 

prime_info AS (
  SELECT 
    item_type,
    total_sqft_one_batch,
    FLOOR(500000 / total_sqft_one_batch) AS prime_batch_count,
    FLOOR(500000 / total_sqft_one_batch) * item_count AS prime_individual_item_count
  FROM type_grouped
  WHERE item_type = 'prime_eligible'
), 

nonprime_sqft AS (
  SELECT 
    500000 - total_sqft_one_batch * prime_batch_count AS remaining_sqft_nonprime
  FROM prime_info
)

SELECT 
  item_type,
  prime_individual_item_count AS item_count
FROM prime_info
UNION
SELECT
  item_type,
  FLOOR((SELECT * FROM nonprime_sqft) / total_sqft_one_batch) * item_count AS item_count 
FROM type_grouped
WHERE item_type = 'not_prime'  
ORDER BY 1 DESC
  
  