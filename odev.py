#soru1: kullanicidan iki sayi alip dört islem ve diger matematik islemlerini yapiyoruz.
#kullanici sayi1 ve sayi2'yi giriyor ve toplama, cikarma, carpma, bolme, mod alma ve us alma islemlerini yapip ekrana yazdiriyoruz.
"""""
sayi1 = int(input("bir sayi giriniz:"))
sayi2 = int(input("bir sayi giriniz:"))

print(f"toplama: {sayi1 + sayi2}")
print(f"cikarma: {sayi1 - sayi2}")
print(f"carpma: {sayi1 * sayi2}")
print(f"bolme: {sayi1 / sayi2}")
print(f"mod: {sayi1 & sayi2}")
print(f"us alma: {sayi1 ** sayi2}")
"""
#soru2:1'den girilen sayiya kadar olan sayilarin toplamini hesaplama.
#kullanici bir sayi giriyor ve 1'den o sayiya kadar olan sayilarin toplamini hesaplayip ekrana yazdiriyoruz.
"""
sayi = int(input("bir sayi girin:"))
toplam = 0
for i in range (1,sayi+1):
    toplam += i
print(f"1'den {sayi} 'e kadar olan sayilarin toplami= {toplam}")   
"""
#soru3:1'den 100'e kadar olan sayilardan sadece cift olanlari ekrana yazdirma.
#1'den 100'e kadar olan sayilardan sadece cift olanlari ekrana yazdiriyoruz.

""""
for i in range(1,101):
    if i % 2 == 0:
        print(i,end=" ")
print()
"""
#soru4:girilen metnin tersini ekrana yazdirma.
#kullanici bir metin giriyor ve o metnin tersini ekrana yazdiriyoruz.
"""""
metin = input("bir metin giriniz:")
tersMetin = ""
for karakter in metin:
    tersMetin = karakter  + tersMetin
print(f"ters metin : {tersMetin}")
"""
