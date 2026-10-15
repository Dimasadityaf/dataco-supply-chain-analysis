"""
Script: clean_data.py
Deskripsi: Membersihkan dataset mentah DataCo, menyaring 28 kolom pilihan,
           menstandarkan format tanggal, serta mengekspor data ke:
           1. dataco_clean.csv (lokal uncompressed untuk Looker Studio)
           2. data/dataco_clean.csv.gz (terkompresi untuk GitHub)
           3. dataco.db (database SQLite untuk analisis SQL)
"""

import os
import sqlite3
import pandas as pd

def main():
    raw_path = os.path.join("data_raw", "DataCoSupplyChainDataset.csv")
    csv_clean_path = "dataco_clean.csv"
    gz_clean_path = os.path.join("data", "dataco_clean.csv.gz")
    sqlite_db_path = "dataco.db"

    print("=" * 60)
    print("1. MEMBACA DATASET MENTAH...")
    print(f"Path: {raw_path}")
    df = pd.read_csv(raw_path, encoding="latin-1")
    initial_rows, initial_cols = df.shape
    print(f"-> Berhasil dimuat: {initial_rows:,} baris, {initial_cols} kolom.")

    # Bersihkan spasi di sekitar nama kolom mentah
    df.columns = df.columns.str.strip()

    # Pemetaan 28 kolom yang dipertahankan
    column_mapping = {
        "Order Id": "order_id",
        "Order Item Id": "order_item_id",
        "order date (DateOrders)": "order_date",
        "Shipping date (DateOrders)": "shipping_date",
        "Type": "type",
        "Days for shipping (real)": "days_for_shipping_real",
        "Days for shipment (scheduled)": "days_for_shipment_scheduled",
        "Delivery Status": "delivery_status",
        "Late_delivery_risk": "late_delivery_risk",
        "Category Name": "category_name",
        "Department Name": "department_name",
        "Product Name": "product_name",
        "Customer Id": "customer_id",
        "Customer Segment": "customer_segment",
        "Customer Country": "customer_country",
        "Market": "market",
        "Order Region": "order_region",
        "Order Country": "order_country",
        "Order Status": "order_status",
        "Shipping Mode": "shipping_mode",
        "Order Item Quantity": "order_item_quantity",
        "Order Item Discount": "order_item_discount",
        "Order Item Discount Rate": "order_item_discount_rate",
        "Order Item Product Price": "order_item_product_price",
        "Sales": "sales",
        "Order Item Total": "order_item_total",
        "Order Profit Per Order": "order_profit_per_order",
        "Order Item Profit Ratio": "order_item_profit_ratio"
    }

    print("\n2. MENYARING 28 KOLOM & MENGUBAH KE SNAKE_CASE...")
    actual_cols_lower = {c.lower(): c for c in df.columns}
    selected_cols = []
    rename_dict = {}

    for target_col, snake_col in column_mapping.items():
        key = target_col.lower()
        if key in actual_cols_lower:
            actual_name = actual_cols_lower[key]
            selected_cols.append(actual_name)
            rename_dict[actual_name] = snake_col
        else:
            raise KeyError(f"Kolom target '{target_col}' tidak ditemukan di dataset mentah!")

    df_clean = df[selected_cols].rename(columns=rename_dict).copy()
    print(f"-> Berhasil disaring: {df_clean.shape[1]} kolom.")

    print("\n3. MENSTANDARKAN FORMAT TANGGAL KE YYYY-MM-DD HH:MM:SS...")
    df_clean["order_date"] = pd.to_datetime(df_clean["order_date"]).dt.strftime("%Y-%m-%d %H:%M:%S")
    df_clean["shipping_date"] = pd.to_datetime(df_clean["shipping_date"]).dt.strftime("%Y-%m-%d %H:%M:%S")
    print("-> Format tanggal selesai dikonversi.")

    print("\n4. MENGEKSPOR FILE HASIL BERSIH...")
    # 4a. CSV lokal uncompressed (Looker Studio)
    df_clean.to_csv(csv_clean_path, index=False, encoding="utf-8")
    csv_size_mb = os.path.getsize(csv_clean_path) / (1024 * 1024)
    print(f"-> [OK] {csv_clean_path} ({csv_size_mb:.2f} MB)")

    # 4b. CSV Gzip compressed (GitHub)
    df_clean.to_csv(gz_clean_path, index=False, compression="gzip", encoding="utf-8")
    gz_size_mb = os.path.getsize(gz_clean_path) / (1024 * 1024)
    print(f"-> [OK] {gz_clean_path} ({gz_size_mb:.2f} MB)")

    # 4c. Database SQLite lokal
    conn = sqlite3.connect(sqlite_db_path)
    df_clean.to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()
    db_size_mb = os.path.getsize(sqlite_db_path) / (1024 * 1024)
    print(f"-> [OK] {sqlite_db_path} ({db_size_mb:.2f} MB, tabel 'orders')")

    print("\n" + "=" * 60)
    print("5. VERIFIKASI ANGKA KUNCI:")
    total_rows = len(df_clean)
    distinct_orders = df_clean["order_id"].nunique()
    distinct_customers = df_clean["customer_id"].nunique()
    distinct_products = df_clean["product_name"].nunique()
    late_count = (df_clean["late_delivery_risk"] == 1).sum()
    late_pct = (late_count / total_rows) * 100
    negative_profit_rows = (df_clean["order_profit_per_order"] < 0).sum()
    total_sales = df_clean["sales"].sum()
    total_profit = df_clean["order_profit_per_order"].sum()

    print(f"- Total Baris Data       : {total_rows:,} (Harus 180,519)")
    print(f"- Pesanan Unik (Order ID): {distinct_orders:,} (Target 65,752)")
    print(f"- Pelanggan Unik         : {distinct_customers:,} (Target 20,652)")
    print(f"- Produk Unik            : {distinct_products:,} (Target 118)")
    print(f"- Pengiriman Terlambat   : {late_count:,} ({late_pct:.2f}%)")
    print(f"- Baris Profit Negatif   : {negative_profit_rows:,} (Target 33,784)")
    print(f"- Total Sales (Kotor)    : ${total_sales:,.2f}")
    print(f"- Total Profit Bersih    : ${total_profit:,.2f}")
    print("=" * 60)
    print("PEMBERSIHAN DATA SELESAI DENGAN SUKSES!")

if __name__ == "__main__":
    main()
