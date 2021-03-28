# sebuah tanggal mempunyai tahun t, bulan b dan hari h
class Tanggal:
	def __init__(self, t, b, h):
		self.t = t
		self.b = b
		self.h = h


# simpan jumlah hari seluruh bulan dari januari sampai dengan desember
hariperbulan = [31, 28, 31, 30, 31, 30,
			31, 31, 30, 31, 30, 31]


# fungsi untuk menghitung jumlah tahun kabisat
def hitungKabisat(h):
	tahun = h.t

	# cek jika tahun ini dianggap sebagai kabisat atau tidak
	if (h.b <= 2):
		tahun = tahun - 1

	# tahun kabisat adalah tahun dengan kelipatan 4, 400 dan bukan kelipatan 100
	return int(tahun / 4) - int(tahun / 100) + int(tahun / 400)


# fungsi untuk mencari jumlah hari dari dua tangggal
def deltaHari(tgl1, tgl2):

	# hitung jumlah hari sebelum tanggal pertama
	# inisaiasi perhitungna menggunakantahun dan hari
	n1 = tgl1.t * 365 + tgl1.h

	# tambahhkan hari untuk bulan dari tanggal yg diberikan
	for i in range(0, tgl1.b - 1):
		n1 = n1 + hariperbulan[i]

	# karena setiap tahun kabisat adalah 366 hari, tambahkan 1 hari untuk setiap tahun kabisat
	n1 = n1 + hitungKabisat(tgl1) 

	# persis sama, hitung jumlah total hari sebelum 'tgl2'
	n2 = tgl2.t * 365 + tgl2.h
	for i in range(0, tgl2.b - 1):
		n2 = n2 + hariperbulan[i]
	n2 = n2 + hitungKabisat(tgl2)

	# hitung perbedaaan hari tgl2 - tgl1
	return (n2 - n1)


masukan1 = input ("Masukkan tanggal pertama (yyyy-mm-dd) :")
masukan2 = input ("Masukkan tanggal kedua (yyyy-mm-dd): ")

tahun1,  bulan1, hari1 = masukan1.split("-")
tahun2,  bulan2, hari2 = masukan2.split("-")


tgl1 = Tanggal (int (tahun1), int (bulan1), int(hari1))
tgl2 = Tanggal (int (tahun2), int (bulan2), int(hari2))
print ("Perbedaan harinya adalah: ", deltaHari(tgl1, tgl2), "hari")
