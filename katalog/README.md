# katalog

Folder ini berisi file-file dan konfigurasi penting dalam berjalannya aplikasi katalog-bella.

Link menuju aplikasi Heroku katalog-bella yang sudah dideploy -> https://katalog-bella.herokuapp.com/katalog/

## Bagan Request client

![New Flowchart](https://user-images.githubusercontent.com/112465346/189484162-ab242e47-0897-48da-9ec2-9326f63e1f59.png)

## Virtual Environment

Virtual Environment adalah tools untuk membuat lingkungan python virtual yang terisolasi. Terisolasi artinya tertutup dan tidak bisa diakses dari dunia luar dan tidak mengganggu file-file lain yang tidak di gunakan. Kita menggunakan virtual environment karena menjaga ruang terpisah untuk sebuah proyek dengan pustaka dan dependensi di satu tempat. Environment ini spesifik ke proyek tertentu dan tidak berinterfer dengan dependensi proyek lainnya.

Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita masih dapat bekerja tanpa virtual environment, yang perlu Anda lakukan yaitu menginstal perpustakaan secara global.Jika kita tidak mengaktifkan virtual environment pada proyek kita maka paket-paket atau modul akan diambil dari site-packages alias global environment. Namun, hal ini bisa menjadi masalah jika Anda memiliki banyak proyek pada mesin yang sama karena bisa conflict dengan sistem modules dan settings anda.

## Pengimplementasian 

1. Pada tugas ini yang dilakukan adalah 
Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Pengimplementasian:
Cara saya mengimplementasikan 4 poin di atas adalah dengan mengimplementasikan apa yang sudah saya pelajari pada lab 0 dan lab 1. Untuk poin 1 sampai 3 saya sudah mempelajarinya pada saat lab 1 (tutorial 1) sehingga pengimplementasian pada tugas ini yaitu dengan melakukan langkah-langkah yang sama seperti lab 1 dan tentu saja dengan berbagai penyesuaian berhubung yang dibuat adalah aplikasi yang berbeda. Selanjutnya untuk poin 4 saya melakukan deployment dengan mengimplementasikan pengetahuan yang telah saya dapat dari lab 0 tentang deployment ke Heroku agar setelah di deploy link bisa di akses secara umum.
