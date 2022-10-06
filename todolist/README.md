## Link 
- Link menuju todolist page -> https://katalog-bella.herokuapp.com/todolist/

- Link menuju register page -> https://katalog-bella.herokuapp.com/todolist/register

- Link menuju login page -> https://katalog-bella.herokuapp.com/todolist/login

- Link menuju create task page -> https://katalog-bella.herokuapp.com/todolist/create-task

- Link menuju logout page -> https://katalog-bella.herokuapp.com/todolist/logout


## Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>```?
  - CSRF (Cross-Site Request Forgery) adalah jenis serangan keamanan web untuk mendapatkan atau mengirim request kepada suatu aplikasi website (misal: submit suatu form) secara illegal yaitu tidak melalui form yang ada di website tersebut secara langsung, sehingga aplikasi tersebut mengeksekusi suatu tindakan yang sebenarnya tidak dikehendaki oleh pengguna internet. Serangan CSRF dapat terjadi disebabkan karena tidak ada mekanisme perlindungan token keamanan (request token) pada sebuah website, sehingga penyerang dapat mengirim suatu request. Untuk itu penting sekali untuk menerapkan mekanisme perlindungan CSRF (CSRF Protection). Potongan kode di atas adalah salah satu mekanisme perlindungan csrf. 
  - Token tersebut diterapkan untuk menghindari serangan berbahaya. CSRF token menghasilkan token di sisi server saat merender halaman dan memeriksa ulang token yang didapat untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. Dengan tambahan sederhana ini, serangan CSRF dapat dihindari, sehingga menjamin keamanan request dari pengguna ke server.
 - Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
 Tanpa CSRF token, request pengguna tidak memiliki kode token yang kompleks sehingga peretas dapat mengeksploitasi celah ini untuk melakukan aktivitas yang tidak diinginkan seperti mengubah data seperti profil pribadi, alamat email, bahkan yang lebih berbahaya melakukan transaksi transfer dana.
 
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }})```?
   Kita tetap bisa membuat elemen <form> secara manual tanpa menggunakan generator karena sebenarnya syntax dari html sendiri sudah bisa mendasari pembuatan elemen form. Tetapi django menyediakan template atau generator yang membuat kita mengimplementasikan pembuatan form dengan lebih sederhana dan mudah.
 Gambaran pembuatan <form> secara manualnya adalah sebagai berikut:
   - pembuatan form pada html harus diawali dan diakhiri tag form seperti berikut  
   ```
   <form action="<http-request>" method="post">
   ...isi form...
   </form>
   ```
   - form tersebut dapat diisi tipe data input yang sesuai dengan menambahkan tag input, misalnya ```<input type="text" id="title>``` dan membuat button bertipe submit dengan misalnya ```<button type="submit">Submit</button>``` sehingga saat user menekan button tersebut, value yang di masukan input akan dikirimkan sesuai action dan method yang ditentukan.

    
    
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
- User memasukkan input dihalaman form html, yang pada aplikasi todolist form juga terdapat pada halaman login
  User memasukkan input username dan password, kemudia fungsi yang ada di ```views.py``` akan mengambil data tersebut dangan menggunakan perintah dibawah ini dan kemudian fungsi tersebut akan meredirect ke html yang diinginkan.
    ``` 
    username = request.POST.get("username")
    password = request.POST.get("password")
    ```
  
    
- contoh lain, misalnya pada saat melakukan create task, user memasukan input judul dan deskripsi, lalu fungsi ```create_task``` yang ada di ```views.py``` akan mengambil value data dari form dengan menggunakan perintah berikut
    ```
    judul = request.POST.get("judul")
    deskripsi = request.POST.get("deskripsi")
    ```
    Kemudian di redirect menuju fungsi utama yaitu ```show_todolist``` yang menampilkan todolist.html, kemudian ```show_todolist``` akan lanjut memanggil fungsi render untuk merender semua objek dalam context dan memasukkannya kedalam todolist.html
    


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

  ![image](https://user-images.githubusercontent.com/112465346/192507854-205357df-330b-4a29-8806-b386d3e3ef70.png)
 
  ![image](https://user-images.githubusercontent.com/112465346/192508320-aae23fe2-c70f-4454-a98c-1a61c7196b01.png)


## Tugas 5 PBP
## Perbedaan Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
| Inline CSS | Internal CSS | External CSS |
| ------------- | ------------- | --------- |
| Inline CSS adalah adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HMTL mempunyai atribut style. Di situlah inline CSS ditulis. | Internal CSS adalah kode CSS yang ditulis dalam tag<style> dan kode HTML yang ditulis di bagian header file HTML. Internal CSS digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan di halaman website yang lain. | External CSS adalah kode CSS yang ditulis terpisah dari kode HTML. External CSS ditulis di sebuah file khusus menggunakan ekstensi .css. File external CSS umumnya diletakkan setelah bagian <head> di halaman. |
| Cukup membantu ketika hanya ingin menguji dan melihat perubahan pada satu elemen.  | Perubahan Internal CSS hanya berlaku di satu halaman saja.| Ukuran halaman jadi lebih kecil dan struktur HTML menjadi lebih rapi, loading website lebih cepat.  |
Berguna untuk memperbarui kode dengan cepat. Proses request HTTP yang kecil membuat proses loading website jadi lebih cepat.| Tidak perlu mengupload banyak file karena HTML dan CSS berada di satu file yang sama.| File CSS dapat digunakan pada beberapa halaman website sekaligus.  |
| Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.| Tidak efisien jika unutk menggunakan CSS yang sama dalam banyak file. Performa web jadi lambat, karena CSS yang berbeda-beda dapat mengakibatkan loading ulang setiap berganti halaman website. | Ketika file CSS gagal dipanggil oleh file HTML, tampilan website akan terlihat berantakan. Salah satu sebabnya adalah koneksi internet yang lambat.|

##  Tag HTML5
- ```<nav>``` -> membuat navigasi bar pada website
- ```<footer>``` -> membuat footer section pada website
- ```<header>``` -> membuat header section pada website
- ```<main>``` -> membuat main content pada website
- ```<input>``` -> membuat sebuah kontrol input

## CSS selector
1. Selektor class : Selektor class adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya.
2. Selektor ID : Selektor ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja. Selektor ID ditandai dengan tanda pagar (#) di depannya.
3. Selector Tag : Selektor Tag disbut juga Type Selector. Selektor ini akan memilih elemen berdasarkan nama tag.

## Implementasi checklist tugas 5
- Menambahkan tag <link> dan <script> pada base.html untuk menggunakan bootstrap
     ![image](https://user-images.githubusercontent.com/112465346/194207127-80833d16-d65a-4483-a389-7955bc3510c5.png)
- Kustomisasi templates untuk halaman login, register, dan create-task memanfaatkan tag dan syntax bootstrap dan diimplementasikan di login.html, register.html, create_task.html, todolist.html
- Pada tugas kali ini saya menggunakan boottrap sehingga halaman website nya sudah menjadi auto responsive

  
  
  

  
  
  
