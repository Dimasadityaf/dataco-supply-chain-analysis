-- 3. Profit menurut kombinasi pasar dan wilayah.
SELECT
    market,
    order_region,
    SUM(sales) AS total_sales,
    SUM(order_profit_per_order) AS total_profit,
    ROUND(
        100.0 * SUM(order_profit_per_order) / NULLIF(SUM(sales), 0),
        2
    ) AS profit_margin_percentage,
    COUNT(DISTINCT order_id) AS total_orders
FROM orders
GROUP BY market, order_region
ORDER BY total_profit DESC;

-- 4. Kontribusi penjualan dan margin laba menurut segmen pelanggan.
SELECT
    customer_segment,
    SUM(sales) AS total_sales,
    SUM(order_profit_per_order) AS total_profit,
    ROUND(
        100.0 * SUM(order_profit_per_order) / NULLIF(SUM(sales), 0),
        2
    ) AS profit_margin_percentage,
    COUNT(DISTINCT order_id) AS total_orders
FROM orders
GROUP BY customer_segment
ORDER BY total_sales DESC;
