bulan_hari = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
bulan_hari_kabisat = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]


def cek_tahun_kabisat(tahun):
	# tahun kabisat adalah tahun dengan kelipatan 4, 400 dan bukan kelipatan 100
	if tahun % 4 == 0:
		if tahun % 100 == 0 : 
			if tahun % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False


#tgl1 = input ("Masukkan tanggal pertama (yyyy-mm-dd) :")
#tgl2 = input ("Masukkan tanggal kedua (yyyy-mm-dd): ")

# Driver program
masukan1 = input ("Masukkan tanggal pertama (yyyy-mm-dd) :")
masukan2 = input ("Masukkan tanggal kedua (yyyy-mm-dd): ")
#masukan1 = "2020-02-11"
#masukan2 = "2022-02-12"

tahun1, bulan1, hari1 = masukan1.split("-")
tahun2, bulan2, hari2 = masukan2.split("-")


def deltaHari (tgl1,tgl2) :
	if cek_tahun_kabisat(int (tahun1)) == True :
		n1 = int (tahun1) * 365 + int (hari1)

		# tambahhkan hari untuk bulan dari tanggal yg diberikan
		for i in range(0, int (bulan1) - 1):
			n1 = n1 + bulan_hari_kabisat[i]
	else :
		n1 = int (tahun1) * 365 + int (hari1)

		# tambahhkan hari untuk bulan dari tanggal yg diberikan
		for i in range(0, int (bulan1) - 1):
			n1 = n1 + bulan_hari[i]

	if cek_tahun_kabisat(int (tahun2)) == True :
		n2 = int (tahun2) * 365 + int (hari2)

		# tambahhkan hari untuk bulan dari tanggal yg diberikan
		for i in range(0, int (bulan2) - 1):
			n2 = n2 + bulan_hari_kabisat[i]
	else :
		n2 = int (tahun2) * 365 + int (hari2)

		# tambahhkan hari untuk bulan dari tanggal yg diberikan
		for i in range(0, int (bulan2) - 1):
			n2 = n2 + bulan_hari[i]

	# hitung perbedaaan hari tgl2 - tgl1
	return (n2 - n1)


delta = deltaHari (masukan1,masukan2)
print ("Beda hari: ",delta)



