# 📦 DataCo Smart Supply Chain & Logistics Profitability Analysis

Proyek analisis data end-to-end untuk mengevaluasi efisiensi pengiriman rantai pasok (*supply chain*) dan profitabilitas finansial menggunakan dataset **DataCo Smart Supply Chain** (periode Januari 2015 – Januari 2018).

---

## 📌 Latar Belakang Proyek
Perusahaan e-commerce/retail modern menghadapi tantangan ganda: menjaga ketepatan waktu pengiriman sekaligus mempertahankan margin keuntungan yang sehat. Keterlambatan pengiriman berpotensi memicu pembatalan dan penurunan kepuasan pelanggan, sementara pemberian diskon yang tidak tepat dapat menyebabkan transaksi bernilai profit negatif.

Proyek ini bertujuan mengidentifikasi titik rawan keterlambatan logistik, memetakan wilayah dan kategori produk dengan profit negatif, serta mendeteksi potensi risiko transaksi mencurigakan (*fraud*).

---

## 🎯 Pertanyaan Bisnis (Business Questions)

Analisis dilakukan secara bertahap menggunakan SQL dalam 4 tingkatan kompleksitas:

### Level 1: Dasar Logistik & Penjualan (Agregasi & Filter)
1. **Mode Pengiriman**: Mode pengiriman mana yang memiliki persentase keterlambatan pengiriman tertinggi?
2. **Kinerja Kategori**: Kategori produk apa yang menghasilkan volume penjualan (*Sales*) terbesar?

### Level 2: Profitabilitas Wilayah & Segmen (HAVING & CASE WHEN)
3. **Pasar & Wilayah**: Pasar (*Market*) dan wilayah (*Region*) mana yang menyumbang profit tertinggi, dan wilayah mana yang mengalami kerugian (*loss*) terbesar?
4. **Segmen Pelanggan**: Bagaimana perbandingan kontribusi penjualan dan margin laba antara segmen *Consumer*, *Corporate*, dan *Home Office*?

### Level 3: Tren Waktu & Pola Musiman (Fungsi Tanggal & CTE)
5. **Tren Pendapatan & Laba**: Bagaimana pola tren penjualan dan profitabilitas bulanan sepanjang tahun 2015 hingga awal 2018?
6. **Musiman Keterlambatan**: Apakah terdapat bulan-bulan tertentu dengan lonjakan rasio keterlambatan pengiriman (*seasonality*)?

### Level 4: Manajemen Risiko & Optimasi Produk (Window Functions & Analisis Lanjutan)
7. **Produk Rugi per Kategori**: Produk spesifik apa saja yang menghasilkan profit paling negatif di setiap kategori produk? *(menggunakan window function `DENSE_RANK()`)*
8. **Double Risk (Rugi & Terlambat)**: Berapa banyak pesanan yang mengalami kerugian finansial sekaligus mengalami keterlambatan pengiriman?
9. **Deteksi Transaksi Mencurigakan**: Berapa total nilai transaksi yang berstatus `SUSPECTED_FRAUD` dan di pasar mana frekuensi fraud tertinggi terjadi?

---

## 📊 Kamus Data (28 Kolom Terpilih)

Dataset mentah terdiri dari 180.519 baris dan 53 kolom. Setelah proses seleksi data dan pembersihan privasi (PII), 28 kolom kunci berikut yang digunakan:

| No | Kolom (*snake_case*) | Tipe Data | Deskripsi |
| :---: | :--- | :--- | :--- |
| 1 | `order_id` | INTEGER | ID unik pesanan pelanggan |
| 2 | `order_item_id` | INTEGER | ID unik item barang dalam pesanan (Primary Key) |
| 3 | `order_date` | DATETIME | Tanggal dan waktu pesanan dibuat (`YYYY-MM-DD HH:MM:SS`) |
| 4 | `shipping_date` | DATETIME | Tanggal dan waktu barang dikirim (`YYYY-MM-DD HH:MM:SS`) |
| 5 | `type` | TEXT | Metode pembayaran (DEBIT, TRANSFER, PAYMENT, CASH) |
| 6 | `days_for_shipping_real` | INTEGER | Jumlah hari riil pengiriman |
| 7 | `days_for_shipment_scheduled` | INTEGER | Target jadwal hari pengiriman |
| 8 | `delivery_status` | TEXT | Status pengiriman (Late delivery, Shipping on time, Advance shipping, Shipping canceled) |
| 9 | `late_delivery_risk` | INTEGER | Indikator keterlambatan (1 = Terlambat, 0 = Tepat Waktu) |
| 10 | `category_name` | TEXT | Nama kategori produk |
| 11 | `department_name` | TEXT | Nama departemen produk |
| 12 | `product_name` | TEXT | Nama spesifik produk |
| 13 | `customer_id` | INTEGER | ID unik pelanggan |
| 14 | `customer_segment` | TEXT | Segmen pelanggan (Consumer, Corporate, Home Office) |
| 15 | `customer_country` | TEXT | Negara asal pelanggan |
| 16 | `market` | TEXT | Pasar tujuan pengiriman (Europe, LATAM, Pacific Asia, USCA, Africa) |
| 17 | `order_region` | TEXT | Wilayah geografis pengiriman pesanan |
| 18 | `order_country` | TEXT | Negara tujuan pesanan |
| 19 | `order_status` | TEXT | Status pesanan (COMPLETE, PENDING, CLOSED, CANCELED, SUSPECTED_FRAUD, dll.) |
| 20 | `shipping_mode` | TEXT | Metode pengiriman (Standard Class, First Class, Second Class, Same Day) |
| 21 | `order_item_quantity` | INTEGER | Jumlah kuantitas produk yang dipesan |
| 22 | `order_item_discount` | REAL | Nilai nominal potongan harga (diskon) |
| 23 | `order_item_discount_rate` | REAL | Persentase diskon yang diberikan |
| 24 | `order_item_product_price` | REAL | Harga satuan produk sebelum diskon |
| 25 | `sales` | REAL | Total nilai kotor transaksi item (`quantity * price`) |
| 26 | `order_item_total` | REAL | Total penerimaan bersih setelah diskon |
| 27 | `order_profit_per_order` | REAL | Keuntungan/kerugian bersih yang dihasilkan item |
| 28 | `order_item_profit_ratio` | REAL | Rasio profit terhadap nilai transaksi |

---

## 🛠️ Alat & Teknologi
- **Bahasa Pemrograman & Pengolahan Data**: Python (Pandas)
- **Database & Query**: SQLite
- **Visualisasi & Business Intelligence**: Looker Studio
- **Version Control & Dokumentasi**: Git & GitHub

---

## 📁 Struktur Repositori
```text
dataco-supply-chain-analysis/
├── README.md               # Ringkasan portofolio & temuan bisnis
├── .gitignore              # Konfigurasi proteksi data mentah & lokal
├── data/
│   ├── dataco_clean.csv.gz # Dataset bersih terkompresi (untuk GitHub)
│   └── data_dictionary.csv # Kamus data format CSV
├── scripts/
│   └── clean_data.py       # Skrip pembersihan & pembentukan database SQLite
├── sql/
│   ├── level1_dasar.sql            # Query SQL Level 1
│   ├── level2_profit_wilayah.sql   # Query SQL Level 2
│   ├── level3_tren_bulanan.sql     # Query SQL Level 3
│   └── level4_window_function.sql  # Query SQL Level 4
├── dashboard/
│   └── screenshot.png      # Tangkapan layar dashboard Looker Studio
└── docs/
    └── kesimpulan_bisnis.md# Laporan analitis & rekomendasi manajerial
```

---

## 📈 Alur Kerja Proyek
- [x] **Fase 0: Persiapan Proyek & Repositori Git**
- [x] **Fase 1: Pemahaman Data & Rumusan Masalah Bisnis**
- [x] **Fase 2: Pembersihan Data & Ekstraksi SQLite (Python)**
- [x] **Fase 3: Eksplorasi & Analisis Data Menggunakan SQL (Level 1–4)**
- [ ] **Fase 4: Perancangan Dashboard Interaktif (Looker Studio)**
- [ ] **Fase 5: Sintesis Temuan & Rekomendasi Bisnis**
- [ ] **Fase 6: Finalisasi & Publikasi Portofolio**
