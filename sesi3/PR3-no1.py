#membuat class permainan video games
class Player:
    #class attribute
    nama_game = "Age of Empire"
    user = "Manusia"

    #buat instance attribute nama dan level
    def __init__(self, nama, level):
        self.nama = nama
        self.level = level

    #instance method intro
    def intro(self):
        print(self.nama + " (Level " + self.level + ")")

    #classmethod
    @classmethod
    def pause (cls):
        print (f" {Player.nama_game} sedang Pause")
    
    @staticmethod
    def running ():
        print (f" {Player.nama_game} sedang running")

#Inheritance
class Pemula (Player):
    # overiding
    user = "Anak-anak"
    
    
    def Aksi (self):
        print (f"Level {Pemula.level} adalah level pemula dengan jumlah kemenangan > 10")

    #overloading
    def intro (self,agresifitas=None):
        if agresifitas == None :
            print ("Pemain baru")
        else:
            print ("Pemain lama")
    

class Medium (Player):
    #overiding
    user = "remaja"
    def Aksi (self):
        print (f"Level {Medium.level} adalah level medium dengan jumlah kemenangan > 50")

class Expert (Player):
    #overiding
    user = "Dewasa"
    
    def Aksi (self):
        print (f"Level {Expert.level} adalah level expert dengan jumlah kemenangan > 100")

#Input Nama dan Level untuk Player
nama = input("Masukkan Nama:")
level = input ("Masukkan Level:")

#proses Instantiate
Player1 = Player(nama, level)
Player1.intro()
print ("Bermain di game: ",Player1.nama_game)

#pemanggilan classmethod
Player1.pause()

#pemanggilan staticmethod
Player1.running()