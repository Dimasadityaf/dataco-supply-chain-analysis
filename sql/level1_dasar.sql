-- Level 1: Dasar logistik dan penjualan
-- Jalankan query pada database SQLite yang memiliki tabel `orders`.

-- 1. Persentase baris pesanan berisiko terlambat menurut mode pengiriman.
SELECT
    shipping_mode,
    COUNT(*) AS total_order_items,
    SUM(CASE WHEN late_delivery_risk = 1 THEN 1 ELSE 0 END) AS late_order_items,
    ROUND(
        100.0 * SUM(CASE WHEN late_delivery_risk = 1 THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0),
        2
    ) AS late_delivery_percentage
FROM orders
GROUP BY shipping_mode
ORDER BY late_delivery_percentage DESC, total_order_items DESC;

-- 2. Kategori produk dengan nilai penjualan kotor terbesar.
SELECT
    category_name,
    SUM(sales) AS total_sales,
    SUM(order_item_quantity) AS units_sold,
    COUNT(*) AS total_order_items
FROM orders
GROUP BY category_name
ORDER BY total_sales DESC;
