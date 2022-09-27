## Link 
- Link menuju todolist page -> https://katalog-bella.herokuapp.com/todolist/

- Link menuju register page -> https://katalog-bella.herokuapp.com/todolist/register

- Link menuju login page -> https://katalog-bella.herokuapp.com/todolist/login

- Link menuju create task page -> https://katalog-bella.herokuapp.com/todolist/create-task

- Link menuju logout page -> https://katalog-bella.herokuapp.com/todolist/logout


## Apa kegunaan {% csrf_token %} pada elemen <form>?
 
  
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?

  
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.


## Implementasi
- Membuat suatu aplikasi baru bernama todolist
  Menggunakan syntax django: 
  ```python manage.py startapp wishlist```
  
- Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
  Menambahkan path untuk todolist di file urls.py yang ada di folder project_django
  ![image](https://user-images.githubusercontent.com/112465346/192491817-bd343f48-ea6e-498f-bdc2-f95ddbc7f58e.png)
  
- Membuat sebuah model Task yang memiliki atribut user, date, title, description
  Membuat atribut dengan data field yang sesuai di dalam models.py
  ![image](https://user-images.githubusercontent.com/112465346/192491988-b287c790-ce56-4e29-831e-fccee72dca6a.png)
  
- Mengimplementasikan form registrasi, login, dan logout
  Pertama-tama membuat fungsi untuk pengaplikasian form di views.py, lalu membuat file html agar di fungsi yang ada di views.py bida diredirect ke file yang sesuai dengan benar dan menambahkan path yang sesuai di urls.py yang ada di folder todolist
  ![image](https://user-images.githubusercontent.com/112465346/192493019-75e8b494-ecf6-4ba4-aa5d-a9a3473ba090.png)
  
  ![image](https://user-images.githubusercontent.com/112465346/192493163-c3045b31-811f-4cf2-9677-ad5fc29982a3.png)

- Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
Membuat file todolist.html yang berisi ketentuan, kemudian membuat fungsi di fungsi show_todolist pada views.py dipanggil fungsi render dan menjadikan todolist.html sebagai salah satu parameternya.
  
- Membuat halaman form untuk pembuatan task.
  Pertama-tama membuat fungsi create_task pada views.py, lalu membuat create_list.html sesuai ketentuan untuk pembuatan task, lalu pada fungsi create_task dipanggil fungsi render dan menjadikan create_task.html sebagai salah satu parameternya
  
- Membuat routing
membuat routing dengan membuat path yang di urls.py seperti berikut
![image](https://user-images.githubusercontent.com/112465346/192506994-e4ee2508-c402-4d5c-82b7-d8768b990e5a.png)
 
- Melakukan deployment ke Heroku terhadap aplikasi yang sudah dibuat
Berhubung saya menggunakan aplikasi dan repositori github yang sama seperti tugas 2, yang saya lakukan hanyalah push ke repositori github terkait sehingga sudah otomatis terdeploy, karena saat tugas 2 saya sudah melakukan deploy dengan cara connect ke repositori github tersebut.
  
- Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

  
  
  

  
  
  
