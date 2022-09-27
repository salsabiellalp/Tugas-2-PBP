- Link HTML -> https://katalog-bella.herokuapp.com/mywatchlist/html

- Link JSON -> https://katalog-bella.herokuapp.com/mywatchlist/json

- link XML -> https://katalog-bella.herokuapp.com/mywatchlist/xml

## Perbedaan antara JSON, XML, dan HTML
| HTML | JSON | XML |
| ------------- | ------------- | --------- |
| HTML (Hypertext Markup Language) adalah bahasa markup yang digunakan untuk membuat halaman website. HTML memerlukan pembuka maupun penutup tag dan mendukung banyak jenis encoding | JSON digunakan untuk menyimpan informasi dengan cara yang terorganisir dan mudah diakses. JSON berbasis markup laguage dan digunakan untuk data delivery atau transfer data. JSON tidak memerlukan pembuka maupun penutup tag dan JSON mendukung semua browser dan sebagian besar teknologi backend mendukung JSON, tetapi ukungan tool pengembangan terbatas DAN Hanya mendukung encoding UTF-8.| XML adalah bahasa markup yang dirancang untuk menyimpan data. Ini populer digunakan atau transfer data. XML Berbasis notasi objek dalam JavaScript dan juga digunakan untuk data delivery atau transfer data. XML memerlukan pembuka maupun penutup tag Dengan bantuan XML, pertukaran data dilakukan dengan cepat antara platform yang berbeda. Jadi, ini membuat dokumen dapat dipindahkan ke seluruh sistem dan aplikasi. Sintaks XML terkadang bisa membingungkan karena mirip dengan alternatif lain dan terkadang berlebihan. |

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Front End dan Back End adalah dua hal yang berkaitan dengan bagaimana sebuah website maupun aplikasi dapat bekerja dan diakses oleh pengguna. Berkaitan dengan proses web development, front end adalah apa yang pengguna lihat pada tampilan sebuah website, sedangkan back end adalah sistem di balik layar yang mengolah database dan juga server. Di bagian backend data diolah dan disusun sedemikian rupa dengan oleh pengembang backend untuk dilakukan delivery data dari backend ke sisi frontend agar pengguna bisa melihat isi tampilan website, sehingga proses data delivery sangatlah penting. Proses data delivery tidak bisa melakukan pertukaran data antara backend dan frontend secara langsung melainkan harus melalu perantara, yang dalam kasus aplikasi repositori ini, JSON dan XML dapat menjadi perantara pertukaran data ke HTML. 

## implementasi
- Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
menggunakan syntax django:
```python manage.py startapp wishlist```

- Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
menambahkan path untuk mywatchlist di file urls.py yang ada di folder project_django

![jango](https://user-images.githubusercontent.com/112465346/191591742-cd61b55a-26fa-46b5-811c-da44b40ec172.png)

- Membuat sebuah model MyWatchList yang memiliki beberapa atribut:
membuat atribut dengan data field yang sesuai di dalam models.py

![models](https://user-images.githubusercontent.com/112465346/191591946-f904353f-482d-48e1-a150-3955647307ae.png)

- Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
Membuat file json dan memasukkan data field sesuai atribut yang ada di models.py. Berikut adalah contoh saya memasukkan 1 objek kedalam file json:

![obj](https://user-images.githubusercontent.com/112465346/191591348-594188f9-7c32-475f-8a35-728e48bea7e9.png)

- Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format: HTML, XML, JSON
Dilakukan dengan cara membuat fungsi untuk menampilkan dalam format HTML,JSON, dan XML di dalam views.py

![show](https://user-images.githubusercontent.com/112465346/191591001-52111a8d-de5d-429c-bd40-cee31a95d549.png)

- Membuat routing sehingga data di atas dapat diakses melalui URL
membuat routing dengan membuat path di urls.py

![routing](https://user-images.githubusercontent.com/112465346/191590663-80d00c59-3974-4562-b762-d79534572488.png)

- Melakukan deployment ke Heroku
Saya menggunakan aplikasi dan repositori github yang sama seperti tugas 2, sehingga yang saya lakukan hanyalah push ke repositori github terkait sehingga sudah otomatis terdeploy, karena saat tugas 2 saya sudah melakukan deploy dengan cara connect ke repositori github tersebut.

- Membuat unit test
dengan cara membuat beberapa fungsi test di dalam tests.py

![tse](https://user-images.githubusercontent.com/112465346/191592517-79ffbe21-b7e4-4b87-80fb-6ea2aa396c07.png)


- Implementasi bonus
Membuat program kondisional didalam views.py dan memasukkan data yang di dapat ke variabel context, lalu dikirim ke HTML dengan memanggil fungsi render

![bonus](https://user-images.githubusercontent.com/112465346/191590040-26965eae-005e-471a-a9ef-cdcbbc598d5c.png)

## Mengakses URL menggunakan Postman

![postman_json](https://user-images.githubusercontent.com/112465346/191438366-2ccb09d5-e700-4838-8d3d-75b77f8e2bc3.png)

![postman_xml](https://user-images.githubusercontent.com/112465346/191438405-4a0205c3-b0c9-45c4-acce-a5881987a578.png)

![postman_html](https://user-images.githubusercontent.com/112465346/191438448-fcffdc13-2757-4480-b396-3ef0f2d036f7.png)
