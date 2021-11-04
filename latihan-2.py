#**Rumus Luas & Keliling Lingkaran**

Luas     = π × r²
Keliling = 2 x π × r

Nilai Phi yang akan kita gunakan adalah 3.14
r merupakan jari-jari lingkaran
Phi merupakan nilai konstanta di matematika sementara jari-jari merupakan jarak antara titik pusat dengan tepi lingkaran.

Selanjutnya kita memerlukan nilai jari-jari (r) yang nantinya akan di masukan pada layar console. 
Kita menggunakan fungsi input() yang nilainya di konversi ke tipe data float (bilangan riil). 
Ingat bahwa fungsi input() akan menganggap semua nilai inputan bertipe string, 
sehingga kita perlu melakukan konversi ke tipe yang diinginkan.

Ketika kita sudah mendapat nilai phi dan jari-jari selanjutnya kita bisa menghitung luas dan keliling sesuai dengan rumus-nya masing-masing
seperti gambar dibawah ini


Selanjutnya kita tampilkan hasilnya dengan fungsi print(). 
sintak \t merupakan karakter espace yang berfungsi untuk membuat tab. 
fungsinya ini agar sejajar karakter sama dengan (=) nya.

Jika dilihat hasil luas dan keliling lingkaran mempunyai angka pecahan yang cukup banyak, 
untuk mengambil 2 angka pecahan saja kita pakai fungsi format() seperti berikut:

print ("Luas Lingkaran \t= ",format(luas,'.2f'))
print ("Keliling Lingkaran \t= ",format(keliling,'.2f'))

maka hasilnya akan jadi seperti dibawah ini

Luas Lingkaran          =  40.72
Keliling Lingkaran      =  22.62
Dengan penggunaan fungsi format(luas,’.2f’) akan menghasilkan 2 angka pecahan saja.