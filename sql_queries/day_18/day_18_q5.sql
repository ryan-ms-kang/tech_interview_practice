/*
Currently, you're analyzing the highest and lowest open prices for each FAANG stock by month over the years.

For each FAANG stock, display the ticker symbol, the month and year ('Mon-YYYY') with the corresponding highest and lowest open prices.
Ensure that the results are sorted by ticker symbol.
*/

WITH min_max_open AS (  
  SELECT 
    *,
    RANK() OVER (
      PARTITION BY ticker
      ORDER BY open 
    ) AS min_open_rank,
    RANK() OVER (
      PARTITION BY ticker
      ORDER BY open DESC
    ) AS max_open_rank
  FROM stock_prices
)

SELECT 
  m1.ticker,
  TO_CHAR(m1.date, 'Mon-YYYY') AS highest_mth,
  m1.open AS highest_open,
  TO_CHAR(m2.date, 'Mon-YYYY') AS lowest_mth,
  m2.open AS lowest_open
FROM min_max_open m1 
JOIN min_max_open m2 
  ON m1.ticker = m2.ticker
WHERE 
  m1.max_open_rank = 1 AND
  m2.min_open_rank = 1
ORDER BY 1