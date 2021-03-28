"""
x =int (input())
if x % 2 == 0:
    print (x, "habis dibagi dua")
elif x % 3 == 0:
    print (x, "habis dibagi tiga")
elif x % 5 == 0:
    print (x, "habis dibagi lima")
else:
    print (x,"tidak habis dibagi dua, tiga ataupun lima")
"""

bulan = {
    1: "Januari",
    2: "Februari",
    3: "Maret",
    4: "April",
    5: "Mei",
    6: "Juni",
    7: "Juli",
    8: "Agustus",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember"
}
n_bulan = int (input())
nama_bulan = bulan.get(n_bulan, "Bulan diantara 1-12")
print (nama_bulan)