class Kendaraan:
    bahan_bakar = 'Bensin'
    
    def __init__(self, nama, warna, jumlah_roda):
        self.nama = nama
        self.warna = warna
        self.jumlah_roda = jumlah_roda
    
    def maju(self):
        print("Kendaraan", self.nama, "maju")
        
    def mundur(self):
        print("Kendaraan", self.nama, "mundur")
            
    @classmethod
    def isi_bahan_bakar(cls):
        print(cls.bahan_bakar, 'sedang diisi')
        

Kendaraan.isi_bahan_bakar()
