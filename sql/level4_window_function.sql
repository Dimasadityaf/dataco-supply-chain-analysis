-- Level 4: Risiko dan optimasi produk
-- Jalankan query pada database SQLite yang memiliki tabel `orders`.

-- 7. Lima produk dengan profit paling negatif di setiap kategori.
WITH product_profit AS (
    SELECT
        category_name,
        product_name,
        SUM(order_profit_per_order) AS total_profit
    FROM orders
    GROUP BY category_name, product_name
    HAVING SUM(order_profit_per_order) < 0
),
ranked_products AS (
    SELECT
        category_name,
        product_name,
        total_profit,
        DENSE_RANK() OVER (
            PARTITION BY category_name
            ORDER BY total_profit ASC
        ) AS loss_rank
    FROM product_profit
)
SELECT
    category_name,
    product_name,
    total_profit,
    loss_rank
FROM ranked_products
WHERE loss_rank <= 5
ORDER BY category_name, loss_rank, product_name;

-- 8. Jumlah pesanan unik yang sekaligus memiliki profit item negatif
-- dan setidaknya satu item berisiko terlambat.
WITH order_risk AS (
    SELECT
        order_id,
        SUM(order_profit_per_order) AS order_profit,
        MAX(late_delivery_risk) AS has_late_delivery_risk
    FROM orders
    GROUP BY order_id
)
SELECT
    COUNT(*) AS orders_with_loss_and_late_risk
FROM order_risk
WHERE order_profit < 0
  AND has_late_delivery_risk = 1;

-- 9a. Nilai kotor dan penerimaan bersih pada baris berstatus suspected fraud.
SELECT
    SUM(sales) AS suspected_fraud_gross_sales,
    SUM(order_item_total) AS suspected_fraud_net_revenue,
    COUNT(DISTINCT order_id) AS suspected_fraud_orders,
    COUNT(*) AS suspected_fraud_order_items
FROM orders
WHERE order_status = 'SUSPECTED_FRAUD';

-- 9b. Pasar dengan frekuensi pesanan suspected fraud tertinggi.
SELECT
    market,
    COUNT(DISTINCT order_id) AS suspected_fraud_orders,
    COUNT(*) AS suspected_fraud_order_items,
    SUM(sales) AS suspected_fraud_gross_sales
FROM orders
WHERE order_status = 'SUSPECTED_FRAUD'
GROUP BY market
ORDER BY suspected_fraud_orders DESC, market;
