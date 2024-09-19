import pyfiglet
from Simulasyon import adam_asmaca
from Sehirler import sehirler
import random


# Gerekli tanimlamalarin yapilmasi
acilan_kelimeler = []
sehir = (random.choice(sehirler))
cevap = " _ " * len(sehir)
kalan_hak = 6


#Baslangic ekraninin olusturulmasi
print("--------------------------------------------------------------------------------------")
giris_ekrani = pyfiglet.figlet_format("Adam Asmaca",font = "Slant")
print(giris_ekrani)
print("--------------------------------------------------------------------------------------")

bilgi = ("Adam Asmaca oyununa hosgeldiniz.Oyunda Türkiye'nin 81 ilinden herhangi birisini tahmin etmeye calisacaksiniz.\n"
         "6 adet yanlis thmin hakkiniz bulunmaktadir.Basarilar\n"
         "Baslamak icin 'ENTER' tusuna basiniz.")

print()
print("!!!!!!! Bilgilendirme !!!!!!")
print(bilgi)


#Oyunu baslatma
basla = input()

print("!!!   Oyun Basladi  !!!\n")
print("Cevap: " + cevap)


def OyunBittiMi():

    if "_" not in cevap:

        return True


#Oyunun baslangicindan sonuna kadar islendigi kisim
while not OyunBittiMi():

    kalan_hak_kontrol = False
    tahmin = input("Tahmininizi Girin: ").lower()
    cevap = "Cevap:"

    for harf in sehir:

        if harf == tahmin:

            cevap +=" " + tahmin + " "
            acilan_kelimeler.append(tahmin)
            kalan_hak_kontrol = True

        elif harf in acilan_kelimeler:

            cevap += " " + harf + " "

        else:

            cevap += " _ "

#Yanlis harf girilmesi durumunda kontrol false donecektir.Bu durumda kalan_hak 1 azaltilmalidir
    if  not kalan_hak_kontrol:

        if kalan_hak != 0:

            kalan_hak -= 1

        else:

            print("__________  Oyunu Kaybettiniz  _______")

    print(adam_asmaca[kalan_hak])
    print(cevap)
    print(f"Kalan Hak: {kalan_hak}")

#Dongu bittiginde kalan_hak 0 degilse oyun kazanilmistir
if kalan_hak != 0:

    print("________ TEBRİKLER KAZANDINIZ ________")








