def verileri_al_ve_yapilari_olustur(sinif_dagilim_listesi, not_toplam, lise_ogr_say):
   try:
        devam = "e"
        while devam == "e" or devam == "E":
            sinif = int(input("Öğrencinin kaçıncı sınıfta olduğunu giriniz. (1-4 arasında tamsayı): "))
            while sinif not in [1,2,3,4]:
                sinif = int(input("Lütfen geçerli bir sınıf bilgisi giriniz: "))
            genel_not = int(input("Öğrencinin genel not ortalamasını giriniz. (0-100 arasında tamsayı): "))
            while genel_not < 0 or genel_not > 100:
                genel_not = int(input("Lütfen geçerli bir not bilgisi giriniz: "))
            lise_adi = input("Öğrencinin mezun olduğu lisenin adını giriniz: ")

            # Anahtarları öğrencinin mezun olduğu lise adı olan not_toplam ve lise_ogr_say dictionary'lerini dolduruyorum.
            lise_ogr_say[lise_adi] = lise_ogr_say.get(lise_adi, 0) + 1

            if lise_adi in not_toplam:  # if key in dictionary:
                not_toplam[lise_adi] += genel_not
            else:
                not_toplam[lise_adi] = genel_not

            # sinif_dagilim_listesi belirli bir sınıftaki belirli genel not ortalaması aralığına giren ÖĞRENCİ SAYILARINI tutuyor.
            # Not aralıkları ardışık gittiği için genel not ortalamasını formülle listenin indexi olabilecek bir sayıya
            # dönüştürerek iki boyutlu listeyi dolduruyorum.
            if genel_not == 0:
                sinif_dagilim_listesi[sinif-1][0] += 1
            else:
                sinif_dagilim_listesi[sinif-1][(genel_not-1)//10] += 1

            devam = input("Bilgileri girilecek başka bir öğrenci var mı? (e/E/h/H): ")
            while devam not in ["e", "E", "h", "H"]:
                devam = input("Lütfen belirtilen harflerden birini giriniz: ")

   except ValueError:
       print("Lütfen öğrencinin mezun olduğu lisenin adını metinsel, sınıfı ve genel not ortalamasını tamsayı giriniz.")
   except Exception as err:
       print(err)


def lise_bilgilerini_yazdir(not_toplam, lise_ogr_say):
    print("Mezun Olunan Lise Adı              Bölümdeki Öğrenci Say   Not Ortalamaları")
    print("--------------------------------   ---------------------   ----------------")
    for lise_adi in lise_ogr_say:  # for key in dictionary:
        print(format(lise_adi, "32"), end="   ")
        print(format(lise_ogr_say[lise_adi], "21d"), end="   ")
        print(format(not_toplam[lise_adi]/lise_ogr_say[lise_adi], "16.2f"))

def sinif_not_dagilimini_yazdir(sinif_dagilim_listesi, SINIF_SAYISI, NOT_ARALIGI_SAYISI):
    print("Sınıflar     0 - 10 %", end="   ")
    for i in range(1, NOT_ARALIGI_SAYISI):
        print(i*10+1, "-", i*10+10, "%", end="   ")
    print("Öğrenci Say")
    print("---------", end="   ")  # Sınıflar ın altını çizmek için 9
    for sayac in range(NOT_ARALIGI_SAYISI):
        print("---------", end="   ")  # Not aralıklarının altını çizmek için 9
    print(" -----------")  # Öğrenci Say ın altını çizmek için

    # Sütun toplamlarını bulmak için ayrı bir liste oluşturup verileri ekrana yazdırıyorum:
    not_araliklari_toplamlari = [0] * NOT_ARALIGI_SAYISI  # O aralığa giren toplam ÖĞRENCİ SAYILARINI tutan liste.
    for sinif_no in range(SINIF_SAYISI):
        print(sinif_no+1, ". sınıf", end="   ")
        siniftaki_ogrenci_sayisi = sum(sinif_dagilim_listesi[sinif_no])
        if siniftaki_ogrenci_sayisi != 0:
            for aralik_no in range(NOT_ARALIGI_SAYISI):
                print(format(sinif_dagilim_listesi[sinif_no][aralik_no]*100/siniftaki_ogrenci_sayisi, "9.2f"), end="   ")
                not_araliklari_toplamlari[aralik_no] += sinif_dagilim_listesi[sinif_no][aralik_no]
            print(format(siniftaki_ogrenci_sayisi, "12d"))
        else:  # (sinif_no+1). sınıftaki öğrenci sayısı 0 ise:
            for aralik_no in range(NOT_ARALIGI_SAYISI):
                print(format(0, "9.2f"), end="   ")
            print(format(0, "12d"))

    # Sütun toplamlarını yani o aralığa giren toplam öğrencilerin oranını yazdırıyorum:
    genel_top = sum(not_araliklari_toplamlari)  # Tüm bölümdeki öğrenci sayısı
    print("Tüm Bölüm", end="   ")
    for aralik_no in range(NOT_ARALIGI_SAYISI):
        print(format(not_araliklari_toplamlari[aralik_no]*100/genel_top, "9.2f"), end="   ")

    print(format(genel_top, "12d"))


def main():
    SINIF_SAYISI = 4
    NOT_ARALIGI_SAYISI = 10
    # Satırları öğrencinin sınıf numarası, sütunları 10 puanlık genel not ortalaması aralıkları olan iki boyutlu liste:
    sinif_dagilim_listesi = []
    for i in range(SINIF_SAYISI):
        ogr_not_gruplari = [0] * NOT_ARALIGI_SAYISI
        sinif_dagilim_listesi.append(ogr_not_gruplari)

    not_toplam = {}  # Öğrencilerin mezun oldukları liselere göre genel not ortalamalarının TOPLAMINI tutacak olan sözlük.
    lise_ogr_say = {}  # Öğrencilerin mezun oldukları liselere göre sayılarını tutacak olan sözlük.
    verileri_al_ve_yapilari_olustur(sinif_dagilim_listesi, not_toplam, lise_ogr_say)
    lise_bilgilerini_yazdir(not_toplam, lise_ogr_say)
    print()
    print("Bölümümüzdeki her sınıftaki öğrencilerin sayıları ve 10 puanlık genel not ortalaması aralıklarına göre dağılımları:")
    print()
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tNOT ARALIKLARI")
    sinif_not_dagilimini_yazdir(sinif_dagilim_listesi, SINIF_SAYISI, NOT_ARALIGI_SAYISI)

main()