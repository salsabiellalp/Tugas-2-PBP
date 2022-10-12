# Perbedaan asynchronous dan synchronous programming
- Asynchronous programming (multi-thread) adalah merupakan sebuah pendekatan pemrograman yang tidak terikat pada input output (I/O)  protocol. Ini menandakan bahwa pemrograman asynchronous tidak melakukan pekerjaannya secara old style / cara lama yaitu dengan eksekusi baris program satu persatu secara hirarki. Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau dapat kita sebut secara Independen.
- Synchronous programming (single-thread) memiliki pendekatan yang lebih old style. Task akan dieksekusi satu persatu sesuai dengan urutan dan prioritas task. Hal ini memiliki kekurangan pada lama waktu eksekusi karena masing-masing task harus menunggu task lain selesai untuk diproses terlebih dahulu.

# Penerapan paradigma Event-Driven Programming pada JavaScript dan AJAX. 
Event-driven programming merupakan suatu pendekatan dalam programming dimana suatu code dibuat untuk merespon suatu kejadian atau event. Pada tugas kali ini juga diterapkan event driven programming, contohnya pada saat tombol ```Add Task``` diklik maka akan mentrigger suatu fungsi sehingga menyebabkan sebuah event terjadi. Pada hal ini event tersebut adalah munculnya modal pada page todolist.html.

# Jelaskan penerapan asynchronous programming pada AJAX.
AJAX adalah sebuah singkatan dari Asynchronous Javascript and XML dan mengacu pada sekumpulan teknis pengembangan web (web development) yang memungkinkan aplikasi web untuk bekerja secara asynchronous. Artinya browser tidak perlu reload seluruh laman website ketika hanya ada perubahan data yang kecil. AJAX akan mengirimkan request ke server, dan melanjutkan eksekusi tanpa menunggu balasan dari server terlebih dahulu.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
## AJAX GET
- Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
  ![image](https://user-images.githubusercontent.com/112465346/195421476-d6d02634-ab4c-47e5-86bf-f82bb12e8b07.png)

- Buatlah path /todolist/json yang mengarah ke view di urls.py
  ![image](https://user-images.githubusercontent.com/112465346/195421559-b00c357d-0508-4db5-83bf-144160fcff54.png)

- Lakukan pengambilan task menggunakan AJAX GET.
  ![image](https://user-images.githubusercontent.com/112465346/195421752-baf71822-dabb-4f5e-8935-fc63772e333e.png)
 
## AJAX POST
- Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
  
- Buatlah view baru untuk menambahkan task baru ke dalam database.
  ![image](https://user-images.githubusercontent.com/112465346/195422033-0978f3ff-336e-4e3d-aa57-aec1cb6213d1.png)

- Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
  ![image](https://user-images.githubusercontent.com/112465346/195422116-01788aa7-2af9-4afb-bf44-23b0c6ff9214.png)

- Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
- Tutup modal setelah penambahan task telah berhasil dilakukan.
- Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.
  fungsi display_todolist() adalah fungsi untuk merefresh halama todolist.html
  
  ![image](https://user-images.githubusercontent.com/112465346/195422321-99218cc1-8a7e-48ac-98d6-90ed4133f144.png)
