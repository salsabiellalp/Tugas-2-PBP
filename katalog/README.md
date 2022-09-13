# katalog

Folder ini berisi file-file dan konfigurasi penting dalam berjalannya aplikasi katalog-bella.

Link menuju aplikasi Heroku katalog-bella yang sudah dideploy -> https://katalog-bella.herokuapp.com/katalog/

## Bagan Request client

![New Flowchart](https://user-images.githubusercontent.com/112465346/189484162-ab242e47-0897-48da-9ec2-9326f63e1f59.png)

## Virtual Environment

Virtual Environment adalah tools untuk membuat lingkungan python virtual yang terisolasi. Terisolasi artinya tertutup dan tidak bisa diakses dari dunia luar dan tidak mengganggu file-file lain yang tidak di gunakan. Kita menggunakan virtual environment karena menjaga ruang terpisah untuk sebuah proyek dengan pustaka dan dependensi di satu tempat. Environment ini spesifik ke proyek tertentu dan tidak berinterfer dengan dependensi proyek lainnya.

Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita masih dapat bekerja tanpa virtual environment, yang perlu kita lakukan yaitu menginstal perpustakaan secara global. Jika kita tidak mengaktifkan virtual environment pada proyek kita maka paket-paket atau modul akan diambil dari site-packages alias global environment. Namun, hal ini bisa menjadi masalah jika kita memiliki banyak proyek pada mesin yang sama karena bisa conflict dengan sistem modules dan settings kita.

## Pengimplementasian 

Pada tugas ini yang dilakukan adalah:
1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dengan cara mengimport CatalogItem dari models.py dan menggunakan syntax CatalogItem.objects.all() serta mengembalikan data ke dalam sebuah HTML dengan cara mengimport dan memanggil fungsi render().
2. Membuat sebuah routing untuk memetakan fungsi yang telah dibuat pada views.py dengan membuat path yang sesuai pada urls.py untuk mengarahkan ke fungsi yang telah dibuat di views.py
3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template dengan cara load data json dan menyimpannya ke dalam context lalu memanggil fungsi render untuk mengirimnya ke template html.
4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat dengan cara membuat aplikasi baru di heroku dan menghubungkannya ke repositori github terkait seperti yang dilakukan pada lab 0.
