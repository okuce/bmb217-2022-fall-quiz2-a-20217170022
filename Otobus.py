"""
Isim: Mehmet
Soyisim: Solak
Numara: 20217170022
Bolum: Bilgisayar Muhendisligi / 2.Sinif
"""



class Otobus:
    """Otobus bilet satis takip sinifi"""
    plaka:str = ""  # otobus plakasi
    nereden:str = "" # baslangic sehri
    nereye:str = ""  # gidilecek sehir
    koltuk_sayisi:int = 0 # toplam koltuk sayisi
    dolu_koltuk_sayisi:int = 0 # dolu koltuk sayisi

    def __init__(self, plaka, nereden, nereye, koltuk_sayisi):
        """ CONSTRUCTOR
        plaka          otobus plakasi
        nereden        baslangic sehri
        nereye         gidilecek sehir
        koltuk_sayisi  bos koltuk sayisi
        """
        self.plaka = plaka
        self.nereden = nereden
        self.nereye = nereye
        self.koltuk_sayisi = koltuk_sayisi

    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        if self.dolu_koltuk_sayisi < self.koltuk_sayisi:
            self.dolu_koltuk_sayisi = self.dolu_koltuk_sayisi + 1
        
    
    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        if self.dolu_koltuk_sayisi > 0:
            self.dolu_koltuk_sayisi = self.dolu_koltuk_sayisi - 1

    
    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print(f"{self.nereden},{self.nereye},{self.plaka},{self.koltuk_sayisi - self.dolu_koltuk_sayisi},{self.dolu_koltuk_sayisi}")
        


