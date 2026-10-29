# 📋 Laporan Eksekutif: Analisis Rantai Pasok & Profitabilitas DataCo

Dokumen ini menyajikan sintesis analitis menyeluruh yang menggabungkan hasil kueri SQL (Level 1–4) dan temuan visual dari **Looker Studio Dashboard** untuk mengevaluasi efisiensi logistik, performa finansial, serta mitigasi risiko bisnis pada dataset DataCo Smart Supply Chain (Januari 2015 – Januari 2018).

---

## 📌 Ringkasan Eksekutif (Executive Summary)

Sepanjang periode operasional 2015 hingga awal 2018, DataCo mencatat total transaksi kotor (**Gross Sales**) sebesar **$36,8 Juta** dan laba bersih (**Total Profit**) sebesar **$4,0 Juta** dari **65.752 pesanan unik** (180.519 item pesanan), menghasilkan margin keuntungan rata-rata sebesar **10,8%**.

Meskipun performa penjualan dan marjin keuntungan terlihat stabil secara makro, analisis mendalam mengungkapkan tiga titik kritis (*pain points*) yang mengancam kepuasan pelanggan dan efisiensi modal:
1. **Kegagalan SLA Logistik Parah pada Layanan Premium**: Mode pengiriman *First Class* dan *Second Class* mencatat tingkat keterlambatan masing-masing **95,32%** dan **76,63%**.
2. **Double-Risk Exposure (Rugi & Terlambat)**: Sebanyak **7.678 pesanan (11,68% dari total pesanan)** mengalami kerugian finansial sekaligus terlambat dikirim ke pelanggan.
3. **Eksposur Fraud Signifikan**: Transaksi berstatus `SUSPECTED_FRAUD` mencapai nilai kotor **$825.934,94** (1.488 pesanan), dengan konsentrasi tertinggi di pasar Eropa dan Amerika Latin.

---

## 🔍 Temuan Kunci Berdasarkan Data

### 1. Kinerja Logistik & Anomali Mode Pengiriman
Berdasarkan analisis terhadap 180.519 baris item pesanan:

| Mode Pengiriman | Total Item | Item Terlambat | Rasio Keterlambatan | Catatan Kinerja |
| :--- | :---: | :---: | :---: | :--- |
| **First Class** | 27.814 | 26.513 | **95,32%** | Kritis: Pelanggan membayar tarif premium namun hampir pasti terlambat |
| **Second Class** | 35.216 | 26.987 | **76,63%** | Buruk: Lebih dari 3/4 pesanan melewati estimasi jadwal |
| **Same Day** | 9.737 | 4.454 | **45,74%** | Cukup: Hambatan operasional pemenuhan hari yang sama |
| **Standard Class** | 107.752 | 41.023 | **38,07%** | Paling stabil dan mendominasi volume pengiriman (59,7%) |
| **Total / Rata-rata** | **180.519** | **98.977** | **54,83%** | Lebih dari separuh item pengiriman mengalami keterlambatan |

> **Insight Operasional**: Tingginya keterlambatan pada layanan *First Class* dan *Second Class* menunjukkan bahwa target estimasi waktu pengiriman (*scheduled days*) yang dijanjikan terlalu agresif dan tidak realistis bagi mitra kurir/armada logistik.

---

### 2. Profitabilitas Wilayah & Segmen Pelanggan
Distribusi laba dan penjualan menunjukkan kontribusi yang terkonsentrasi pada pasar-pasar tertentu:

* **Dominasi Pasar Regional**:
  * **Europe** menghasilkan laba terbesar (**$1,2 Juta**), dipimpin oleh *Western Europe* ($625,4 rb laba, margin 10,61%).
  * **LATAM** menyumbang laba tertinggi kedua (**$1,1 Juta**), dengan kontributor utama *Central America* ($616,3 rb laba, margin 10,88%) dan *South America* ($335,2 rb laba, margin 11,32%).
  * **Africa** dan kawasan tertentu seperti *Central Asia* memiliki volume transaksi lebih kecil, namun *Southern Africa* membukukan margin profit tertinggi (**13,51%**).
* **Keseragaman Segmen Pelanggan**:
  * Segmen **Consumer** menyumbang 51,9% total penjualan ($19,1 Juta) dan laba $2,07 Juta (margin 10,86%).
  * Segmen **Corporate** menyumbang 30,4% total penjualan ($11,2 Juta) dan laba $1,20 Juta (margin 10,77%).
  * Segmen **Home Office** menyumbang 17,7% total penjualan ($6,5 Juta) dan laba $0,69 Juta (margin 10,59%).
  * *Margin laba di ketiga segmen relatif seragam (~10,6% – 10,8%)*, menandakan bahwa kebijakan penetapan harga dan struktur diskon saat ini belum dibedakan secara strategis antar segmen B2B vs B2C.

---

### 3. Kategori Produk Berkinerja Tinggi vs Marjinal
* **Kategori Penopang Penjualan (Top Sales)**:
  * *Fishing* ($6,93 Juta), *Cleats* ($4,43 Juta), *Camping & Hiking* ($4,12 Juta), *Cardio Equipment* ($3,69 Juta), dan *Women's Apparel* ($3,15 Juta).
* **Kategori Berprofit Marjinal (10 Terendah)**:
  * Kategori seperti *Strength Training* ($332,3 profit), *CDs* ($383,8), *As Seen on TV!* ($714,4), *Books* ($883), dan *Toys* ($900,7) menghasilkan volume dan margin yang sangat tipis dan berpotensi membebani biaya pergudangan (*inventory holding cost*).
* **Produk Merugi (Negative Profit)**:
  * Terdapat produk spesifik yang menghasilkan akumulasi kerugian akibat pemberian diskon berlebih atau penetapan harga jual di bawah biaya pemenuhan (*fulfillment cost*), seperti `SOLE E35 Elliptical` pada kategori *Strength Training* (rugi bersih -$965,12).

---

### 4. Manajemen Risiko: Double Risk & Penipuan (Fraud)
* **Double Risk Orders**:
  * **7.678 pesanan unik (11,68%)** mencatat transaksi bernilai profit negatif dan sekaligus mengalami keterlambatan pengiriman. Kondisi ini merupakan skenario terburuk bagi e-commerce (*kehilangan margin uang dan mengecewakan pelanggan secara bersamaan*).
* **Deteksi Transaksi Mencurigakan (`SUSPECTED_FRAUD`)**:
  * Total **1.488 pesanan** terindikasi fraud dengan nilai kotor **$825.934,94**.
  * Pasar dengan frekuensi fraud tertinggi adalah **Europe** (426 pesanan, $252,3 rb) dan **LATAM** (398 pesanan, $237,2 rb), diikuti **Pacific Asia** (369 pesanan, $172,1 rb).

---

## 💡 Rekomendasi Bisnis & Rencana Aksi (Actionable Roadmap)

### Rekomendasi 1: Kalibrasi Ulang SLA & Evaluasi Mitra Kurir Premium (Prioritas: Tinggi)
* **Masalah**: Keterlambatan *First Class* mencapai 95,3% merusak reputasi brand dan memicu klaim pengembalian ongkos kirim.
* **Tindakan**:
  1. Sesuaikan estimasi target hari pengiriman (*scheduled shipping days*) pada sistem pemesanan online agar sesuai dengan realitas rantai pasok aktual (misal: tambah buffer 1–2 hari).
  2. Lakukan audit performa dan negosiasi ulang kontrak Service Level Agreement (SLA) dengan operator logistik pihak ketiga (3PL). Tetapkan penalti kompensasi bagi keterlambatan pengiriman paket kelas ekspres.

### Rekomendasi 2: Penerapan Kebijakan Batas Diskon Dinamis (Dynamic Discount Throttling)
* **Masalah**: Produk bernilai tinggi seperti alat olahraga sering dijual merugi akibat diskon persentase tinggi yang memakan seluruh margin kotor.
* **Tindakan**:
  1. Pasang sistem validasi (*guardrail*) pada sistem checkout: diskon tidak boleh melebihi margin kotor produk (*floor price protection*).
  2. Alihkan strategi promosi dari potongan harga langsung (*flat discount*) menjadi *bundled promotion* atau poin loyalitas untuk produk berbobot berat/biaya kirim tinggi.

### Rekomendasi 3: Pengetatan Verifikasi Pembayaran & Deteksi Dini Fraud (Prioritas: Sedang)
* **Masalah**: Potensi kebocoran pendapatan hingga ~$826 ribu akibat transaksi *suspected fraud*, terutama di kawasan Eropa dan Amerika Latin.
* **Tindakan**:
  1. Terapkan protokol verifikasi ketat (3D Secure, Address Verification Service/AVS) untuk pesanan bernilai di atas $500 pada gateway pembayaran di pasar Eropa dan LATAM.
  2. Tahan proses *dispatch* logistik (*hold fulfillment*) selama 2–4 jam untuk pesanan dengan skor risiko tinggi guna memungkinkan verifikasi manual oleh tim *Risk & Compliance*.

### Rekomendasi 4: Rasionalisasi Portofolio Produk & Optimalisasi Gudang
* **Masalah**: Kategori dengan penjualan dan profit mikro mengikat ruang simpan dan modal kerja.
* **Tindakan**:
  1. Terapkan strategi *Just-in-Time* (JIT) atau sistem dropshipping untuk kategori dengan profit rendah (*Strength Training, CDs, Toys*).
  2. Alokasikan kapasitas gudang utama di Western Europe dan Central America untuk produk perputaran cepat (*fast-moving, high-margin*) seperti *Fishing, Cleats*, dan *Camping & Hiking*.

---

## 🎯 Kesimpulan
DataCo memiliki fondasi pasar internasional yang kuat dengan profitabilitas rata-rata 10,8%. Namun, efisiensi operasional logistik—khususnya pemenuhan janji layanan pengiriman cepat—merupakan area pembenahan paling mendesak. Dengan merevisi SLA kurir, membatasi diskon yang menggerus profit, dan memperketat filter deteksi fraud, DataCo dapat mempertahankan loyalitas pelanggan sekaligus menaikkan margin laba secara signifikan.
