def movie_stats (judul,jumlah, harga_tiket,*kota):
    pendapatan = jumlah*harga_tiket
    print ("Tiket film " , judul," terjual sebanyak", jumlah," dengan total pendapatan Rp.",pendapatan," di kota ",kota)

movie_stats ("Spiderman", 100, 50000, "Jakarta, Surabaya" )
movie_stats ("Ironman",300,10000,"Jakarta, Surabaya, Malang")
