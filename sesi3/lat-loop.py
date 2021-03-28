
i = 1
while i<=5 :
    print (i)
    i = i + 1

print ("Selesai")
"""
print ("====Coba While Minus")

i = 3
while i>= 0:
    print (i)
    i -=1

print("Selesai While Minus")

print ("\n")
print ("===Coba While with IF===")
x= 1
while x < 10:
    if x%2==0 :
        print ( str (x) + " angka genap")
    else :
        print (str(x) + " angka ganjil")
    x+=1

print ("===Selesai while ganjil genap===")


print ("===Game Hit and Miss===")
point = 100
i = 0
while i < 4 :
    masukan = input()
    if masukan =="hit":
        nilai_hit = 10
    elif masukan =="miss":
        nilai_hit = -20
    else :
        nilai_hit = 0
    point  = point + nilai_hit
    i= i+1

print (point)


print ("===Loop dalam Tuple (Tukur)===")
# Tagihan
tagihan = [50000, 75000, 125000, 300000, 200000]
# Tanpa menggunakan while loop
total_tagihan = tagihan[0] + tagihan[1] + tagihan[2] + tagihan[3] + tagihan[4]
print(total_tagihan)

# Dengan menggunakan while loop
i = 0 # sebuah variabel untuk mengakses setiap elemen tagihan satu per satu
jumlah_tagihan = len(tagihan) # panjang (jumlah elemen dalam) list tagihan
total_tagihan = 0 # mula-mula, set total_tagihan ke 0
while i < jumlah_tagihan: # selama nilai i kurang dari jumlah_tagihan
    total_tagihan += tagihan[i] # tambahkan tagihan[i] ke total_tagihan
    i += 1 # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya.
print(total_tagihan)


print ("===Tagihan Minus====")
tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < jumlah_tagihan:
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # pengulangan akan dihentikan
    if tagihan[i] < 0:
        total_tagihan = -1
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan[i]
    i += 1
print(total_tagihan)



print ("===Lewati tagihan minus===")
tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
i = 0
jumlah_tagihan = len(tagihan)
total_tagihan = 0
while i < len (tagihan):
    # jika terdapat tagihan ke-i yang bernilai minus (di bawah nol),
    # abaikan tagihan ke-i dan lanjutkan ke tagihan berikutnya
    if tagihan[i] <0:
        i += 1
        continue
    total_tagihan += tagihan[i]
    i += 1
print(total_tagihan)



print ("===Latihan Loop FOR===")
list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan: # untuk setiap tagihan dalam list_tagihan
    total_tagihan += tagihan # tambahkan tagihan ke total_tagihan
print(total_tagihan)


print ("===Latihan loop For in case ada minus===")
list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan:
    if tagihan <0:
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan
print(total_tagihan)


print ("===List Cashflow loop For")
list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan +=dana
    else:
        total_pengeluaran +=dana
total_pengeluaran *= -1
print(total_pengeluaran) 
print(total_pemasukan)
"""

# print ("===Latihan While Break ===")
# sum = 0
# i = 0
# while True:
#     i = i+1
#     x= input("Masukkan input ke-" + str(i) + ":" ) 
#     if x == "stop":
#         break

#     sum = sum + int (x)

# print (sum)
