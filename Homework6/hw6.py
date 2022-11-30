HATA_MESAJI = "Hatalı veri, lütfen tekrar giriniz: "
MIN_AY_NO = 1 #Ocak
MAX_AY_NO = 12 #Aralık

def ay_no_al():
    ay_no = int(input("İşlem yapmak istediğiniz tarihin ay numarasını giriniz: "))
    while ay_no < MIN_AY_NO or ay_no > MAX_AY_NO: #ay_no 1 ile 12 arasında olmalıdır.
        ay_no = int(input(HATA_MESAJI))
    return ay_no

def artik_yil_al():
    artik_yil_mi = input("Bu ayın ait olduğu yıl, artık yıl mı? (e/E/h/H): ")
    while artik_yil_mi not in ["E","e","H","h"]: #Girilen karakterler bunlardan biri değilse tekrar alınmalıdır.
        artik_yil_mi = input(HATA_MESAJI)
    if artik_yil_mi == "E" or artik_yil_mi == "e": #Girilen karakter E veya e ise artik_yil değişkenine True atanır.
        artik_yil = True
    else: #Girilen karakter H veya h ise artik_yil değişkenine False atanır.
        artik_yil = False
    return artik_yil #artik_yil değişkeni geriye döndürülür.

def gun_no_al(ay_no, artik_yil):
    gun_no = int(input("Gün numarasını giriniz: "))
    # Ocak(1),Mart(3),Mayıs(5),Temmuz(7),Ağustos(8),Ekim(10) ve Aralık(12) 31 gündür. Kullanıcı buna uygun değerler girmeli.
    if ay_no in [1,3,5,7,8,10,12]:
        while gun_no <= 0 or gun_no > 31:
            gun_no = int(input(HATA_MESAJI))
    # Nisan(4),Haziran(6),Eylül(9) ve Kasım(11) 30 gündür. Kullanıcı buna uygun değerler girmeli.
    elif ay_no in [4,6,9,11]:
        while gun_no <= 0 or gun_no > 30:
            gun_no = int(input(HATA_MESAJI))
    # Eğer bu elif'e giriyorsa ay_no 2 olmak zorundadır yani ay Şubat'tır. Diğer aylar olsaydı üstteki iflere girip seçme yapısından çıkardı.
    elif artik_yil: #ay_no 2 iken artik_yil bool tipi değişkenin değeri True ise Şubat 29 gündür.
        while gun_no <= 0 or gun_no > 29:
            gun_no = int(input(HATA_MESAJI))
    else: #ay_no 2 ve artik_yil False ise else'e sapar ve Şubat 28 gündür.
        while gun_no <= 0 or gun_no > 28:
            gun_no = int(input(HATA_MESAJI))
    return gun_no

def tekrar_al():
    devam_mi = input("Başka bir tarih için hesaplama yapmak ister misiniz? (e/E/h/H): ")
    while devam_mi not in ["e","E","h","H"]: #Girilen karakter bunlardan biri değilse tekrar alınmalıdır.
        devam_mi = input(HATA_MESAJI)
    if devam_mi == "E" or devam_mi == "e": #Girilen karakter E veya e ise devam değişkenine True atanır.
        devam = True
    else: #Girilen karakter H veya h ise devam değişkenine False atanır.
        devam = False
    return devam #devam değişkeninin değeri geriye döndürülür.

def main():
    devam = True
    while devam: #devam değişkeninde True olduğu sürece döngü döner. Döngünün sonunda tekrar_al() fonksiyonu ile kullanıcıya sorulur.
        ay_no = ay_no_al()
        artik_yil = artik_yil_al()
        gun_no = gun_no_al(ay_no,artik_yil)

        gecen_gun_say = gun_no #Sonradan eklememek için toplam değişkeninin ilk değerine kullanıcıdan alınan gun_no'yu atadım.

        for ay in range(1,ay_no): #ay değişkeni 1'den ay_no'ya(dahil değil) kadar birer birer artarak ilerlerken herbir dönüşünde:
            if ay in [1,3,5,7,8,10]: #Bu aylardan biri ise bu aylar 31 gün olduğu için geçen gün sayısına 31 ekledim.
                gecen_gun_say += 31
            elif ay in [4,6,9,11]: #Bu aylardan biri işe bu aylar 30 gün olduğu için geçen gün sayısına 30 ekledim.
                gecen_gun_say += 30
            elif artik_yil: #Bu yıl artık yılsa Şubat 29 gün olduğu için geçen gün sayısına 29 ekledim.
                gecen_gun_say += 29
            else: #Bu yıl artık yıl değilse Şubat 28 gün olduğu için geçen gün sayısına 28 ekledim.
                gecen_gun_say += 28

        print("Yılbaşından bu tarihe kadar geçen gün sayısı:", gecen_gun_say)
        devam = tekrar_al()

main()



