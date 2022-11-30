UCRETSIZ_KULLANIM_SURESI = 1 #ay
toplam_kullanici = 0
memnun_kullanici = 0
notr_kullanici = 0 # Uygulamadan ne memnun ne değil olan kullanıcıların sayısı
memnun_olmayan_kullanici = 0
ios_kullanicisi = 0
android_kullanicisi = 0
ios_toplam_puan = 0
android_toplam_puan = 0
uzun_sureli_kullanici = 0 # Uygulamayı 1 yıldan (12ay) daha uzun süre kullanan kullanıcıların sayısı
uzun_sureli_toplam_sure = 0 # Uzun süreli kullanıcıların uygulamayı kullandığı toplam süre
uzun_sureli_toplam_puan = 0
memnun_olmayan_toplam_sure = 0 # Memnun olmayan kullanıcıların uygulamayı kullandığı toplam süre
erken_silen_kullanici = 0 # Uygulamayı ücretsiz kullanım süresi dolmadan silen kullanıcı sayısı

devam = "e"
while devam == "e":
    isletim_sistemi = input("Kullanıcının cihazındaki işletim sistemini giriniz (i: ios, a: android): ")
    kullanilan_sure = int(input("Kullanıcının uygulamayı kullandığı süreyi giriniz (ay sayısı): "))
    memnuniyet_duzeyi = int(input("Kullanıcının uygulamadan memnuniyet düzeyini giriniz (1: memnun değil, 2: ne memnun ne memnun değil, 3: memnun): "))
    toplam_kullanici += 1
    if memnuniyet_duzeyi == 1: # Kullanıcı memnun değil ise
        memnun_olmayan_kullanici += 1
        memnun_olmayan_toplam_sure += kullanilan_sure
        if isletim_sistemi == "i":
            ios_kullanicisi += 1
            ios_toplam_puan += 1
        else:
            android_kullanicisi += 1
            android_toplam_puan += 1
    elif memnuniyet_duzeyi == 2: # Kullanıcı ne memnun ne memnun değil ise
        notr_kullanici += 1
        if isletim_sistemi == "i":
            ios_kullanicisi += 1
            ios_toplam_puan += 2
        else:
            android_kullanicisi += 1
            android_toplam_puan += 2
    else: #Kullanıcı memnun ise
        memnun_kullanici += 1
        if isletim_sistemi == "i":
            ios_kullanicisi += 1
            ios_toplam_puan += 3
        else:
            android_kullanicisi += 1
            android_toplam_puan += 3

    if kullanilan_sure > 12: # Uzun süreli kullanıcı ise
        uzun_sureli_kullanici += 1
        uzun_sureli_toplam_sure += kullanilan_sure
        if memnuniyet_duzeyi == 1:
            uzun_sureli_toplam_puan += 1
        elif memnuniyet_duzeyi == 2:
            uzun_sureli_toplam_puan += 2
        else:
            uzun_sureli_toplam_puan += 3

    if kullanilan_sure < UCRETSIZ_KULLANIM_SURESI:
        erken_silen_kullanici += 1
    devam = input("Başka kullanıcı var mı? (e/h): ")

print("Uygulamadan memnun olan kullanıcıların sayısı:", memnun_kullanici,
      "ve yüzdesi: %", format(memnun_kullanici*100/toplam_kullanici,".2f"))
print("Uygulamadan ne memnun ne memnun değil olan kullanıcıların sayısı:", notr_kullanici,
      "ve yüzdesi: %", format(notr_kullanici*100/toplam_kullanici,".2f"))
print("Uygulamadan memnun olmayan kullanıcıların sayısı:", memnun_olmayan_kullanici,
      "ve yüzdesi: %", format(memnun_olmayan_kullanici*100/toplam_kullanici,".2f"))
print("IOS kullanıcılarının oranı: %", format(ios_kullanicisi*100/toplam_kullanici,".2f"),
      "ve memnuniyet düzeyi ortalaması:", format(ios_toplam_puan/ios_kullanicisi,".2f"))
print("Android kullanıcılarının oranı: %", format(android_kullanicisi*100/toplam_kullanici,".2f"),
      "ve memnuniyet düzeyi ortalaması:", format(android_toplam_puan/android_kullanicisi,".2f"))
print("Uygulamanın genel memnuniyet düzeyi ortalaması:",
      format((memnun_kullanici*3+notr_kullanici*2+memnun_olmayan_kullanici)/toplam_kullanici,".2f"))
print("Uygulamayı 1 yıldan daha uzun süre kullanan kullanıcıların sayısı:", uzun_sureli_kullanici,
      ", kullandıkları ortalama süre:", format(uzun_sureli_toplam_sure/uzun_sureli_kullanici,".2f"),
      "ay ve memnuniyet düzeyi ortalaması:", format(uzun_sureli_toplam_puan/uzun_sureli_kullanici,".2f"))
print("Uygulamadan memnun olmayan kullanıcıların uygulamayı kullandıkları ortalama süre:",
      format(memnun_olmayan_toplam_sure/memnun_olmayan_kullanici,".2f"),"ay")
print("Uygulamanın ücretsiz kullanım süresi dolmadan silen kullanıcıların tüm kullanıcılar içindeki oranı: %",
      format(erken_silen_kullanici*100/toplam_kullanici,".2f"))
