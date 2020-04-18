print("""
****************************
Faktöriyel Bulma Programı

Çıkmak için q'ya basınız...
****************************
""")

while True:
    sayi = input("Bir sayı girin: ")
    if(sayi =="q"):
        print("Programdan çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        faktoriyel = 1

        for i in range(2,sayi+1):
            faktoriyel *=i

        print(faktoriyel)






