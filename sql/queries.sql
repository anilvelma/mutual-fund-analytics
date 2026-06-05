-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by AMFI Code
SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code;

-- 3. Monthly SIP Inflow Trend
SELECT month,
       total_sip_inflow_crore
FROM monthly_sip_inflows
ORDER BY month;

-- 4. Transactions by State
SELECT state,
       COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio Below 1%
SELECT scheme_name,
       expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Transaction Amount by Transaction Type
SELECT transaction_type,
       AVG(amount_inr) AS avg_amount
FROM investor_transactions
GROUP BY transaction_type;

-- 7. Top 10 Cities by Transactions
SELECT city,
       COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY city
ORDER BY total_transactions DESC
LIMIT 10;

-- 8. Average Returns by Category
SELECT category,
       AVG(return_1yr_pct) AS avg_return_1yr
FROM scheme_performance
GROUP BY category;

-- 9. Portfolio Holdings by Sector
SELECT sector,
       SUM(weight_pct) AS total_weight
FROM portfolio_holdings
GROUP BY sector
ORDER BY total_weight DESC;

-- 10. Benchmark Index Performance
SELECT index_name,
       AVG(index_value) AS avg_index_value
FROM benchmark_indices
GROUP BY index_name;