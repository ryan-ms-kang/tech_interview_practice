/*
Write a query to show sales performance by region and quarter in a pivot table format. 
This question tests to pivot data for reporting purposes.
*/
SELECT
    region,
    SUM(CASE WHEN sales_date BETWEEN '01-01-2025' AND '03-31-2025' THEN amount ELSE 0 END) AS Q1_sales,
    SUM(CASE WHEN sales_date BETWEEN '04-01-2025' AND '06-30-2025' THEN amount ELSE 0 END) AS Q2_sales,
    SUM(CASE WHEN sales_date BETWEEN '07-01-2025' AND '09-30-2025' THEN amount ELSE 0 END) AS Q3_sales,
    SUM(CASE WHEN sales_date BETWEEN '10-01-2025' AND '12-31-2025' THEN amount ELSE 0 END) AS Q4_sales
FROM Sales
GROUP BY 1