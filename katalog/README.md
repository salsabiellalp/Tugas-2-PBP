# katalog

Folder ini berisi file-file dan konfigurasi penting dalam berjalannya aplikasi katalog-bella.

Link menuju aplikasi Heroku katalog-bella yang sudah dideploy -> https://katalog-bella.herokuapp.com/katalog/

## Bagan Request client

![Screenshot 2022-09-15 001702](https://user-images.githubusercontent.com/112465346/190220294-0bac5b82-7f5c-411f-8b9e-991071a78784.png)


## Virtual Environment

Virtual Environment adalah tools untuk membuat lingkungan python virtual yang terisolasi. Terisolasi artinya tertutup dan tidak bisa diakses dari dunia luar dan tidak mengganggu file-file lain yang tidak di gunakan. Kita menggunakan virtual environment karena menjaga ruang terpisah untuk sebuah proyek dengan pustaka dan dependensi di satu tempat. Environment ini spesifik ke proyek tertentu dan tidak berinterfer dengan dependensi proyek lainnya.

Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita masih dapat bekerja tanpa virtual environment, yang perlu kita lakukan yaitu menginstal perpustakaan secara global. Jika kita tidak mengaktifkan virtual environment pada proyek kita maka paket-paket atau modul akan diambil dari site-packages alias global environment. Namun, hal ini bisa menjadi masalah jika kita memiliki banyak proyek pada mesin yang sama karena bisa conflict dengan sistem modules dan settings kita.

## Pengimplementasian 

Pada tugas ini yang dilakukan adalah:
1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dengan cara mengimport CatalogItem dari models.py dan menggunakan syntax CatalogItem.objects.all() serta mengembalikan data ke dalam sebuah HTML dengan cara mengimport dan memanggil fungsi render().

![views py](https://user-images.githubusercontent.com/112465346/190221023-ff2eaaae-eed3-44dc-8cbe-8c2c058cc2de.png)

2. Membuat sebuah routing untuk memetakan fungsi yang telah dibuat pada views.py dengan membuat path yang sesuai pada urls.py untuk mengarahkan ke fungsi yang telah dibuat di views.py

![urls py](https://user-images.githubusercontent.com/112465346/190221371-3506a2f9-d10d-4085-a640-09bce9660034.png)

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template dengan cara load data json dan menyimpannya ke dalam context lalu memanggil fungsi render untuk mengirimnya ke template html.

![context](https://user-images.githubusercontent.com/112465346/190224367-633f50e0-69c5-42f5-b015-0d04c1da3e0c.png) 

dan dipetakan ke file HTML seperti berikut:

![html](https://user-images.githubusercontent.com/112465346/190224765-b21d1183-6c07-41e7-9756-1cb775c26505.png)

4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat dengan cara membuat aplikasi baru di heroku, mengatur API key dan menghubungkannya (connect) ke repositori github terkait dan melakukan re-run failed jobs di github actions seperti yang dilakukan pada lab 0.
