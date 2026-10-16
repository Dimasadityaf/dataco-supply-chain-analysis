-- Level 3: Tren waktu dan pola musiman
-- Jalankan query pada database SQLite yang memiliki tabel `orders`.

-- 5. Tren penjualan dan profitabilitas bulanan dari Januari 2015.
SELECT
    strftime('%Y-%m', order_date) AS order_month,
    SUM(sales) AS total_sales,
    SUM(order_profit_per_order) AS total_profit,
    ROUND(
        100.0 * SUM(order_profit_per_order) / NULLIF(SUM(sales), 0),
        2
    ) AS profit_margin_percentage,
    COUNT(DISTINCT order_id) AS total_orders
FROM orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY order_month;

-- 6. Rasio keterlambatan per bulan pesanan dibuat.
-- Denominator mencakup seluruh baris item yang tercatat pada bulan tersebut.
SELECT
    strftime('%Y-%m', order_date) AS order_month,
    COUNT(*) AS total_order_items,
    SUM(CASE WHEN late_delivery_risk = 1 THEN 1 ELSE 0 END) AS late_order_items,
    ROUND(
        100.0 * SUM(CASE WHEN late_delivery_risk = 1 THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0),
        2
    ) AS late_delivery_percentage
FROM orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY order_month;
