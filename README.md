# Aplikasi Pemesanan Alat Tulis Kantor

## Deskripsi Program

Aplikasi Pemesanan Alat Tulis Kantor adalah aplikasi web sederhana yang dibuat menggunakan **Python dan Django** untuk melakukan proses pemesanan alat tulis kantor.

Aplikasi memungkinkan pengguna mengisi data pelanggan, memilih jenis barang, menentukan jumlah barang, kemudian sistem menghitung total tagihan berdasarkan harga satuan dan jumlah barang yang dipesan.

Hasil pemesanan disimpan ke dalam file **JSON (`data.json`)** sehingga data pesanan dapat tersimpan dan digunakan kembali.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **Django** — framework web yang digunakan untuk membangun aplikasi.
- **HTML** — membuat struktur halaman dan form pemesanan.
- **CSS** — mengatur tampilan dan tata letak halaman.
- **JSON** — media penyimpanan hasil pemesanan.
- **Django Templates** — menampilkan data dari backend ke halaman HTML.

## Penggunaan

### 1. Menyiapkan Project

Pastikan Python dan Django sudah terpasang.

Masuk ke folder project, kemudian jalankan server Django:

```bash
python manage.py runserver
```

### 2. Membuka Aplikasi

Buka browser dan akses:

```text
http://127.0.0.1:8000/
```

### 3. Melakukan Pemesanan

Isi form pemesanan dengan data:

- Nama pelanggan
- Nomor HP
- Jenis barang
- Jumlah barang

Kemudian submit form untuk memproses pesanan.

### 4. Melihat Hasil

Setelah form dikirim, Django akan memproses data dan menampilkan hasil pemesanan, termasuk jumlah barang dan total tagihan setelah perhitungan diskon.

Data pemesanan juga disimpan ke dalam:

```text
data.json
```

## Fitur

### 1. Form Pemesanan

Pengguna dapat memasukkan data pemesanan melalui form yang terdiri dari nama pelanggan, nomor HP, jenis barang, dan jumlah barang.

### 2. Pilihan Jenis Barang

Jenis barang disimpan dalam sebuah struktur data Python dan ditampilkan pada form menggunakan perulangan pada Django Template.

Barang yang tersedia:
- Buku
- Pulpen
- Pensil
- Penghapus

### 3. Pengurutan Jenis Barang

Data jenis barang diurutkan secara ascending atau berdasarkan abjad menggunakan fungsi bawaan Python sebelum ditampilkan pada form.

### 4. Penentuan Harga Otomatis

Django memproses jenis barang yang dipilih dan menentukan harga satuannya menggunakan kontrol percabangan.

### 5. Perhitungan Total Tagihan

Aplikasi memiliki function untuk menghitung total harga berdasarkan harga satuan dan jumlah barang.

Rumus yang digunakan:

```text
Total harga = Harga satuan × Jumlah barang
```

### 6. Perhitungan Diskon

Aplikasi memberikan diskon **10%** apabila total harga lebih dari **Rp 50.000**.

Ketentuannya:

```text
Jika total harga > Rp 50.000
→ Diskon 10%

Jika total harga <= Rp 50.000
→ Tidak mendapatkan diskon
```

### 7. Penyimpanan Data dalam JSON

Hasil pemesanan disimpan dalam file:

```text
data.json
```

Data yang disimpan meliputi informasi pemesanan seperti nama pelanggan, nomor HP, jenis barang, jumlah barang, dan total tagihan.

### 8. Tampilan Hasil Pemesanan

Setelah data diproses oleh Django, aplikasi menampilkan hasil pemesanan kepada pengguna, termasuk total tagihan setelah diskon.

### 9. CSS Eksternal dan Logo

Aplikasi menggunakan CSS eksternal untuk mengatur tampilan halaman serta menggunakan gambar logo sebagai identitas aplikasi.

## Contoh Perhitungan

Misalnya pengguna melakukan pemesanan:

```text
Jenis Barang  : Buku
Jumlah Barang : 20
Harga Satuan  : Rp 5.000
```

Maka:

```text
Total = Rp 5.000 × 20
      = Rp 100.000
```

Karena total harga lebih dari Rp 50.000, pengguna mendapatkan diskon 10%:

```text
Diskon = 10% × Rp 100.000
       = Rp 10.000

Total setelah diskon = Rp 100.000 - Rp 10.000
                     = Rp 90.000
```

Jadi total tagihan yang ditampilkan:

```text
Rp 90.000
```

## Struktur Project

Contoh struktur project Django:

```text
project/
├── manage.py
├── data/
│   └── data.json
├── app/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── templates/
│   └── ...
└── static/
    ├── css/
    │   └── style.css
    └── img/
        └── logo.png
```

