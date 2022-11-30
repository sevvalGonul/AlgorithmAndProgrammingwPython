insan_sayisi = int(input("Şehirde yaşayan insan sayısını giriniz: "))
olgu_sayisi = int(input("Testler sonucu saptanan olgu sayısını giriniz: "))
hasta_sayisi = int(input("Hasta sayısını giriniz: "))

olgu_nufus_orani = round(olgu_sayisi/insan_sayisi * 100, 3)
hastalik_olmayan_olgu = olgu_sayisi-hasta_sayisi
hastalik_olmayan_olgu_oran_olgu = round(hastalik_olmayan_olgu/olgu_sayisi * 100, 3)
AGIR_HASTA_ORANI = 0.15
OLUM_ORANI = 0.02
HAFIF_HASTA_ORANI = 0.85
agir_hasta = round(hasta_sayisi*AGIR_HASTA_ORANI)
olum_sayisi = round(hasta_sayisi*OLUM_ORANI)
hafif_hasta = round(hasta_sayisi*HAFIF_HASTA_ORANI)
toplam_maliyet = insan_sayisi*125+hafif_hasta*1250+agir_hasta*12500
# Test maliyeti = 125Tl, hafif hasta tedavi masrafı = 1250TL, ağır hasta tedavi masrafı=12500TL
kisi_basi_maliyet = round(toplam_maliyet/insan_sayisi, 2)

print("Olgu sayısının nüfusa oranı: %", olgu_nufus_orani)
print("Hatalık belirtisi vermeyen olgu sayısı:", hastalik_olmayan_olgu)
print("Hastalık belirtisi vermeyen olguların tüm olgular içindeki oranı: %", hastalik_olmayan_olgu_oran_olgu)
print("Süreç boyunca karşılaşılacak yaklaşık ağır hasta sayısı:", agir_hasta)
print("Süreç boyunca karşılaşılacak yaklaşık ölüm sayısı:", olum_sayisi)
print("Hastalığın şehir bütçesine getireceği yaklaşık toplam maliyet:", format(toplam_maliyet, ",.2f"), "TL")
print("Hastalığın tüm nüfus dikkate alındığında yaklaşık kişi başı ortalama maliyeti:", kisi_basi_maliyet, "TL")
