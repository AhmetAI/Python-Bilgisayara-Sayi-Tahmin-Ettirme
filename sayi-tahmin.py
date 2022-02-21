import random
import threading
import time

zaman = 0

def sure():
    global zaman
    while (zaman < 1000000):
        zaman = zaman + 1
        time.sleep(1)
    return zaman


def komut():

    karaliste = []

    min_sayi = int(input("Üretilecek Minimum Sayı - "))
    max_sayi = int(input("Üretilecek Maximum Sayı - "))
    bulunacak_sayi = int(input("Bulunacak Sayı -  "))

    if (bulunacak_sayi > max_sayi) or (bulunacak_sayi < min_sayi):
        print("Bulunacak Sayı Maximum/Minimum Sayıdan Fazla/Az Olamaz")
        exit()

    surethreading.start()
    print("Aranıyor...")
    sayı = random.randint(min_sayi, max_sayi)
    if (sayı != bulunacak_sayi):
        karaliste.append(sayı)

    while (sayı != bulunacak_sayi):
        sayı = random.randint(min_sayi, max_sayi)
        if (sayı not in karaliste):
            karaliste.append(sayı)

    print("Denelinen Sayılar :")
    print(karaliste)
    print("Sayı Bulundu")
    print("Minimum Sayı", min_sayi, "\nMaximum Sayı", max_sayi)
    print("Aranılan Sayı ", bulunacak_sayi)
    print(len(karaliste), ". Denemede ",zaman,"Saniyede Bulundu.")
    exit()



surethreading = threading.Thread(target=sure)
komutthreading = threading.Thread(target=komut)

komutthreading.start()
