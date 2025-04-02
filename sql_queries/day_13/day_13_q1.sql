/*
We’d like you to write a query to calculate the annual revenue growth rate for each product line. 
*/

WITH yearly_sales AS (
    SELECT 
        product_line,
        YEAR(sale_date) AS year,
        SUM(revenue) AS total_revenue
    FROM Sales 
    GROUP BY 1, 2
), 

prev_curr_yearly_sales AS (
    SELECT 
        product_line,
        year, 
        total_revenue,
        LAG(total_revenue) OVER(
            PARTITION BY product_line
            ORDER BY year
        ) AS prev_year_revenue
    FROM yearly_sales
)

SELECT 
    *,
    CASE 
        WHEN prev_year_revenue IS NOT NULL THEN ROUND((total_revenue - prev_year_revenue) / prev_year_revenue, 2) * 100
        ELSE NULL 
    END AS growth_rate
FROM prev_curr_yearly_sales;
