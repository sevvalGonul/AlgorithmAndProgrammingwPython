MAX_PUAN = 5 # Kullanıcının bir ürüne verebileceği maximum puan
MIN_PUAN = 1 # Kullanıcının bir ürüne verebileceği minimum puan
SINIR_ORTALAMA_PUAN = 2 # Kullanıcının satın aldığı ürünlere verdiği ortalama puan bundan küçükse ekrana yazdırılacaktır.
SINIR_IADE_SAY = 1 # Kullanıcının iade ettiği ürün sayısı buna eşit veya büyükse ekrana yazdırılacaktır.
max_alis_say = -1 # Max değikeninin başlangıçtaki değerine olamayacak kadar küçük bir sayı atadım.
dusuk_ortalama_veren_kul_say = 0 # Satın aldığı ürünlere verdiği puanların ortalaması sınır ortalama puandan(2'den) düşük olan kullanıcı sayısı
tam_puan_vermeyen_kul_say = 0 # Satın aldığı hiçbir ürüne 5 puan vermeyen kullanıcı sayısı
iade_eden_kul_say = 0 # Sipariş verdiği ürünlerin en az 1 tanesini iade eden kullanıcı sayısı
toplam_iade_say = 0 # Tüm kullanıcıların iade ettiği toplam ürün sayısı
kullanici_say = 0 # Toplam kullanıcı sayısı

kullanici_numarasi = int(input("Lütfen kullanıcı numarasını giriniz.(Başka kullanıcı kalmadıysa 0 ya da 0'dan küçük bir değer giriniz): "))
while kullanici_numarasi > 0:
    siparis_say = int(input("Lütfen kullanıcının sipariş verdiği ürün sayısını giriniz: "))
    while siparis_say <= 0:
        print("Sipariş edilen ürün sayısı 0 ya da negatif olamaz!")
        siparis_say = int(input("Lütfen geçerli bir sipariş sayısı giriniz: "))

    iade_say = int(input("Lütfen kullanıcının iade ettiği ürün sayısını giriniz: "))
    while iade_say > siparis_say or iade_say < 0:
        print("İade edilen ürün sayısı sipariş edilen ürün sayısından büyük veya negatif olamaz!")
        iade_say = int(input("Lütfen geçerli bir iade sayısı giriniz: "))

    toplam_iade_say += iade_say
    alis_say = siparis_say - iade_say # Kullanıcının satın aldığı ürün sayısı
    kullanici_say += 1
    toplam_puan = 0 # Kullanıcının satın aldığı ürünlere verdiği toplam puan
    iyi_urun_say = 0 # Kullanıcının 4 veya 5 puan verdiği ürün sayısı
    tam_puan_verdi = False

    for urun in range(1, alis_say+1):
        puan = int(input("Kullanıcının satın aldığı " + str(urun) + ". ürüne kaç puan verdiğini giriniz. (1-5 arasında): "))
        while puan < MIN_PUAN or puan > MAX_PUAN:
            print("Girdiğiniz puan 1 ile 5 arasında olmalı!")
            puan = int(input("Lütfen ürün için geçerli bir puan giriniz."))
        toplam_puan += puan
        if puan == MAX_PUAN-1: # 4 puan vermişse
            iyi_urun_say += 1
        elif puan == MAX_PUAN: # 5 puan vermişse
            iyi_urun_say += 1
            tam_puan_verdi = True

    ortalama_puan = toplam_puan / alis_say

    print("Kullanıcının sipariş verdiği ürünleri satın alma oranı: %", format(alis_say*100/siparis_say, ".2f"))
    print("Kullanıcının satın aldığı ürünlere verdiği puanların ortalaması:", format(ortalama_puan, ".2f"))
    print("Kullanıcının 4 veya 5 puan verdiği ürünlerin satın aldığı ürünler içindeki oranı: %", format(iyi_urun_say*100/alis_say, ".2f"))

    if iade_say >= SINIR_IADE_SAY: # Sipariş verdiği ürünlerin en az 1 tanesini iade etmişse
        iade_eden_kul_say += 1

    if tam_puan_verdi == False: # Satın aldığı hiçbir ürüne 5 puan vermemişse
        tam_puan_vermeyen_kul_say += 1

    if ortalama_puan < SINIR_ORTALAMA_PUAN: # Satın aldığı ürünlere verdiği puanların ortalaması 2’den düşükse
        dusuk_ortalama_veren_kul_say += 1

    # En çok ürün satın alan kullanıcıyı bulmak için:
    if alis_say > max_alis_say:
        max_alis_say = alis_say # En çok ürün satın alan kullanıcının satın aldığı ürün sayısı
        max_alan_numara = kullanici_numarasi # En çok ürün satın alan kullanıcının kullanıcı numarası
        max_alan_iade_say = iade_say # En çok ürün alan kullanıcının iade ettiği ürün sayısı
        max_alan_ortalama_puan = ortalama_puan # En çok ürün alan kullanıcının aldığı ürünlere verdiği puanların ortalaması

    kullanici_numarasi = int(input("Lütfen kullanıcı numarasını giriniz.(Başka kullanıcı kalmadıysa 0 ya da 0'dan küçük bir değer giriniz): "))

print("Kullanıcı başına iade edilen ortalama ürün sayısı:", round(toplam_iade_say/kullanici_say))
print("Sipariş verdiği ürünlerin en az 1 tanesini iade eden kullanıcı sayısı:", iade_eden_kul_say,
      "ve tüm kullanıcılar içindeki oranı: %", format(iade_eden_kul_say*100/kullanici_say, ".2f"))
print("Satın aldığı hiçbir ürüne 5 puan vermeyen kullanıcı sayısı:", tam_puan_vermeyen_kul_say,
      "ve tüm kullanıcılar içindeki oranı: %", format(tam_puan_vermeyen_kul_say*100/kullanici_say, ".2f"))
print("Satın aldığı ürünlere verdiği puanların ortalaması 2’den düşük olan kullanıcı sayısı:", dusuk_ortalama_veren_kul_say,
      "ve tüm kullanıcılar içindeki oranı: %", format(dusuk_ortalama_veren_kul_say*100/kullanici_say, ".2f"))
print("En çok ürün satın alan kullanıcının numarası:",max_alan_numara,". Bu kullanıcının satın aldığı ürün sayısı:",max_alis_say,
      ", iade ettiği ürün sayısı:", max_alan_iade_say, "ve satın aldığı ürünlere verdiği puanların ortalaması:", format(max_alan_ortalama_puan,".2f"))



