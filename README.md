# Test — Kalkulator CLI

[![CI](https://github.com/Panz-08/Test/actions/workflows/ci.yml/badge.svg)](https://github.com/Panz-08/Test/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Kalkulator sederhana berbasis terminal yang ditulis dengan Python murni (tanpa dependensi).
Proyek ini dipakai sebagai latihan dasar fungsi, percabangan, penanganan input, dan pengujian
otomatis.

## Fitur

- Empat operasi aritmetika: tambah, kurang, kali, dan bagi.
- Input angka desimal (`float`).
- Penanganan input tidak valid tanpa membuat program berhenti.
- Pesan khusus untuk pembagian dengan nol.
- Menu interaktif dengan opsi keluar.

## Menjalankan

Butuh Python 3.10 atau lebih baru.

```bash
python3 kal.py
```

Contoh sesi:

```text
=====================================
  programnya kalkulator panz08 ganz
=====================================
    1. Penjumblahan (+)
    2. pengurangan (-)
    3. Perkalian (*)
    4. Pembagian (/)
    5. Keluar
=====================================
masukkan pilihan anda (1/2/3/4/5): 1
masukkan angka pertama: 12
masukkan angka kedua: 8

Hasil: 12.0 + 8.0 = 20.0
```

## Fungsi

| Fungsi | Keterangan |
| --- | --- |
| `tambah(a, b)` | Mengembalikan `a + b`. |
| `kurang(a, b)` | Mengembalikan `a - b`. |
| `kali(a, b)` | Mengembalikan `a * b`. |
| `bagi(a, b)` | Mengembalikan `a / b`, atau pesan error bila `b == 0`. |

## Test

```bash
python3 -m unittest discover -s tests -v
```

Test dijalankan otomatis lewat GitHub Actions pada setiap push ke `main` dan pull request
(Python 3.10, 3.12, dan 3.13).

## Lisensi

[MIT](LICENSE) © 2026 Panz-08
